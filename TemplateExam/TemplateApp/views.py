from django.shortcuts import render

# Create your views here.

class Member:
  def __init__(self, id, name, join_at, picture_path):
    self.id = id
    self.name = name
    self.join_at = join_at
    self.picture_path = picture_path

members_list = [
  Member(0, 'Taro', '2020/01/01', 'img/taro.jpg'),
  Member(1, 'Jiro', '2020/01/01', 'img/jiro.jpg'),
  Member(2, 'Hanako', '2020/01/01', 'img/hanako.jpg'),
  Member(3, 'Yoshiko', '2020/01/01', 'img/yoshiko.jpg')
]


def home(request):
  return render(request, 'home.html')


def members(request):
  return render(request, 'members.html', context = {
    "members": members_list
  })

def member_details(request, id):
  return render(request, 'member_details.html', context = {
    "member": members_list[id]
  })
