from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'gsplit/index.html')


def profile(request):
    return render(request, 'gsplit/profile.html')


def friends(request):
    return render(request, 'gsplit/friends.html')


def chat(request):
    return render(request, 'gsplit/chat.html')


def create_acc(request):
    return render(request, 'gsplit/create_acc.html')


def login(request):
    return render(request, 'gsplit/login.html')


# def style(request):
#     return render(request, 'gsplit/static/gsplit/style.css')
#
#
# def script(request):
#     return render(request, 'gsplit/static/gsplit/script.js')


