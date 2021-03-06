from django.urls import path,re_path
from . import views, consumer
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='gsplit-index'),
    path('profile/<slug:username>', views.UserProfile.as_view(), name='gsplit-profile'),
    path('edit', views.EditProfile, name='gsplit-edit'),

    path('following', views.Friends.as_view(), name='gsplit-friends'),
    path('follow/<int:pk>', views.follow, name='follow'),
    path('chat', views.chat, name='gsplit-chat'),

    path('', views.HomePageView.as_view(), name='post'),

    path('login', auth_views.LoginView.as_view(template_name ='gsplit/login.html'), name='gsplit-login'),
    path('create_acc', views.createAcc.as_view(), name='gsplit-create_acc'),
    path('logout', auth_views.LogoutView.as_view(), name = 'gsplit-logout'),

    path('test', views.TestPage.as_view(), name='test'),
    path('thanks', views.ThanksPage.as_view(), name='thanks'),

    path('post/<int:pk>/comment/', views.comment_work, name='comment_work'),
    path('post/<int:pk>/likes/', views.likes, name='likes'),

    path('posts', views.PostList.as_view(), name='all'),
    path('new', views.CreatePost.as_view(), name='create'),
    # re_path(r'by/(?P<username>[-\w]+)',views.UserPosts().as_view, name='for_user'),
    # re_path(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.UserPostsDetail.as_view(),name="single"),
    path('chat/<str:room_name>/', views.chatt, name='room'),

    re_path(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumer.ChatConsumer),

]



