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

#COMMENT MODEL IS CURRENTLY BEING WORKED ON, DO NOT SUBMIT SIMILAR TO OTHER SOURCES ONLINE
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CurrentUser,related_name='commenter', on_delete=models.CASCADE)
    content = models.TextField(max_length=160) #Limit User Input to 160 Char
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(CurrentUser)
#COMMENT MODEL IS CURRENTLY BEING WORKED ON, DO NOT SUBMIT SIMILAR TO OTHER SOURCES ONLINE
#Registers in admin.py
#Form start in forms.py
