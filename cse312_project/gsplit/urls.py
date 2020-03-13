from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name='gsplit-home-page'),
    path('profile/', views.profile_page, name='gsplit-profile-page'),
    path('friends/', views.friends_page, name='gsplit-friends-page'),
    path('post/', views.post_page, name='gsplit-post-page')
]