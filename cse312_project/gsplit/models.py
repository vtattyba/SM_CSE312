from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
import misaka



# Create your models here.


class User(auth_models.User, auth_models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)
    
# class UserProfile(models.Model):
#     profile_pic = models.ImageField()
#     user = models.ForeignKey(auth_models.User, unique=True,on_delete=models.CASCADE)
#


CurrentUser = get_user_model()

from django import template
# register = template.library()

class Post(models.Model):
    owner = models.ForeignKey(CurrentUser, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, *kwargs)

    def get_absolute_url(self):
        # return reverse('single',kwargs={'username':self.owner, 'pk':self.pk})
        return reverse('all')

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(CurrentUser, related_name='posts', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date =  models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
