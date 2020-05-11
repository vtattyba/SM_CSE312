from django.contrib import admin
from . import models

from .models import Post, Comment, UserProfile, Follows

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Follows)

