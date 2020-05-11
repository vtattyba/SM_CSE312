from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
import misaka
import uuid
from django.db.models import Count
from django import template
# Create your models here.
CurrentUser = get_user_model()


class User(auth_models.User, auth_models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class Follows(object):
    pass


class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to="images/", blank=True, null=True, default="BlueHead.jpg")
    user = models.OneToOneField(CurrentUser, unique=True, on_delete=models.CASCADE, null=True)
    bio = models.TextField(default="We see you haven't made your profile yet. Go ahead and edit your profile with your information !")
    bio_html = models.TextField(editable=False)
    following = models.ManyToManyField('self', through='Follows', through_fields=('follower', 'followee'), symmetrical=False, related_name='+')
    followers = models.ManyToManyField('self', through='Follows', through_fields=('followee', 'follower'), symmetrical=False, related_name='+')
    def __str__(self):
        # return self.bio
        return self.user.username


class Follows(models.Model):
    followee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name='+')
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name='+') #tg

# register = template.library()


class Post(models.Model):
    owner = models.ForeignKey(CurrentUser, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField(default='')
    message_html = models.TextField(editable=False)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)
    liked = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.message

    def like(self):
        if not self.liked:
            self.likes += 1
        else:
            self.likes -= 1
        self.liked = not self.liked
        return self.likes

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse('all')

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CurrentUser, related_name="commenter", on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        strval = self.text
        return strval
