from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return render(request, 'gsplit/index.html')


def profile_page(request):
    return render(request, 'gsplit/profile.html')


def friends_page(request):
    return render(request, 'gsplit/friends.html')


def post_page(request):
    return render(request, 'gsplit/post.html')
