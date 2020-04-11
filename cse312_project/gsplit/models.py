from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse



# Create your models here.


class User(auth_models.User, auth_models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)
    

GroupUser = get_user_model()

from django import template
# register = template.library()

class Post(models.Model):
    owner = models.ForeignKey(GroupUser, related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        self.message

    def save(self, *args, **kwargs):
        self.message_html = self.message
        super().save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse('single',kwargs={'username':self.owner, 'pk':self.pk})


    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'message']

# class Likers(models.Model):
#     like = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
#     user = models.ForeignKey(GroupUser,related_name='user_likes', on_delete=models.CASCADE)

#     def __str__(self):
#         return "{}".format(self.user)

#     class Meta:
#         unique_together = ("like", "user")