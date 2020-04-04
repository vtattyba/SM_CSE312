from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gsplit-index'),
    path('profile', views.profile, name='gsplit-profile'),
    path('friends', views.friends, name='gsplit-friends'),
    path('create_acc', views.create_acc, name='gsplit-create_acc'),
    path('chat', views.chat, name='gsplit-chat'),
    path('login', views.login, name='gsplit-login'),
    # path('script', views.script, name='gsplit-script'),
    # path('style', views.style, name='gsplit-style'),

]
