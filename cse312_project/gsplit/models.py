from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
import misaka
CurrentUser = get_user_model()

from django import template

# Create your models here.


class User(auth_models.User, auth_models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to="images/", blank=True, null=True, default = "BlueHead.jpg")
    user = models.OneToOneField(CurrentUser, unique=True,on_delete=models.CASCADE, null=True)
    bio = models.TextField(default="We see you haven't made your profile yet. Go ahead and edit your profile with your information !")
    bio_html = models.TextField(editable=False)

    def __str__(self):
        return self.bio

    # def save(self, *args, **kwargs):
    #     self.bio_html = misaka.html(self.bio)
    #     super().save(*args, *kwargs)


# register = template.library()

class Post(models.Model):
    owner = models.ForeignKey(CurrentUser, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)
    liked = models.BooleanField(default=0)
    likes = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.message

    def has_liked(self):
        if self.liked is False:
            self.liked = True
        else:
            self.liked = False

    def like(self):
        if self.liked is False:
            self.likes += 1
            self.liked = True
        else:
            self.likes -= 1
            self.liked = False
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
    author = models.ForeignKey(CurrentUser, related_name="commenter", on_delete=models.CASCADE, blank = True, null = True)
    text = models.TextField(blank = True, null = True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        strval = self.text
        return strval

    # def save(self, *args, **kwargs):
    #     self.text_html = misaka.html(self.text)
    #     super().save(*args, *kwargs)
