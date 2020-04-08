from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    ads = [('gsplit/images/IMG_7781.JPG',
            'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s.'),
           ('gsplit/images/IMG_7781.JPG',
            'Some quick example text to build on the card title and make up the bulk of the card\'s content.'),
           ('gsplit/images/IMG_7781.JPG',
            'Some quick example text to build on the card title and make up the bulk of the card\'s content.')]
    c = {'ads': ads}
    return render(request, 'gsplit/index.html', context=c)


def profile(request):
    return render(request, 'gsplit/profile.html')


def friends(request):

    ads = [('gsplit/images/IMG_7781.JPG', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s.'),
           ('gsplit/images/IMG_7781.JPG', 'Some quick example text to build on the card title and make up the bulk of the card\'s content.'),
           ('gsplit/images/IMG_7781.JPG', 'Some quick example text to build on the card title and make up the bulk of the card\'s content.')]
    c = {'ads': ads}
    return render(request, 'gsplit/friends.html', context=c)


def chat(request):
    return render(request, 'gsplit/chat.html')


def create_acc(request):
    return render(request, 'gsplit/create_acc.html')


def login(request):
    return render(request, 'gsplit/login.html')

