from django import forms
from .models import Theme, Comment

class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class':'border rounded-lg'
            }
        ))

    class Meta:
        model = Theme
        fields = ('title',)


class DeleteThemeForm(forms.ModelForm):

    class Meta:
        model = Theme
        fields = []


class PostCommentForm(forms.ModelForm):
    content = forms.CharField(
        label='comment',
        widget=forms.Textarea(
            attrs={
                'class': 'w-80 h-60'
            }
        ))

    class Meta:
        model = Comment
        fields = ('content',)