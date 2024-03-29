from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.cache import cache
from django.http import Http404, JsonResponse
from .forms import CreateThemeForm, DeleteThemeForm, PostCommentForm
from .models import Theme, Comment
import json


# Create your views here.

def create_theme(request):
  form = CreateThemeForm(request.POST or None)
  if form.is_valid():
    form.instance.user = request.user
    form.save()
    messages.info(request, 'New theme was created.')
    return redirect('boards:list_theme')

  return render(request, 'boards/create_theme.html', context={
    'form': form
  })


def list_theme(request):
  themes = Theme.objects.fetch_all()
  return render(request, 'boards/list_theme.html', context={
    'themes': themes
  })

def edit_theme(request, id):
  theme = get_object_or_404(Theme, id=id)
  if theme.user.id != request.user.id:
    raise Http404
  form = CreateThemeForm(request.POST or None, instance=theme)
  if form.is_valid():
    form.save()
    messages.info(request, 'The theme was edited successfully.')
    return redirect('boards:list_theme')
  
  return render(request, 'boards/edit_theme.html', context={
    'form': form,
    'id': id
  })

def delete_theme(request, id):
  theme = get_object_or_404(Theme, id=id)
  if theme.user.id != request.user.id:
    raise Http404
  form = DeleteThemeForm(request.POST or None, instance=theme)
  if form.is_valid():
    theme.delete()
    messages.info(request, 'The theme was deleted successfully.')
    return redirect('boards:list_theme')
  
  return render(request, 'boards/delete_theme.html', context={
    'form': form,
    'id': id
  })

def post_comment(request, theme_id):
  saved_comment = cache.get(f"{request.user.id}-{theme_id}", '')
  theme = get_object_or_404(Theme, id=theme_id)
  form = PostCommentForm(request.POST or None, initial={'content':saved_comment})
  comments = Comment.objects.fetch_all_by_theme(theme)
  if form.is_valid():
    form.instance.theme = theme
    form.instance.user = request.user
    form.save()
    cache.delete(f"{request.user.id}-{theme_id}")
    return redirect('boards:post_comment', theme_id=theme_id)
  
  return render(request, 'boards/post_comment.html', context={
    'form': form,
    'theme': theme,
    'comments': comments
  })

def save_comment(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      user_id = data.get('user_id')
      theme_id = data.get('theme_id')
      message = data.get('message')
      cache.set(f"{user_id}-{theme_id}", message)
      return JsonResponse({'message': 'Comment saved temporary!'})
    
    except json.JSONDecodeError:
              return JsonResponse({'success': False, 'error': 'Invalid JSON data.'}, status=400)
  else:
      # POSTリクエスト以外の場合
      return JsonResponse({'success': False, 'error': 'Method not allowed.'}, status=405)
