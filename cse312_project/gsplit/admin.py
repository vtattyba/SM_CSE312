from django.contrib import admin
from . import models

from .models import Post, Comment, UserProfile, Follows, Chat

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('name', 'body')
#
#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Follows)
admin.site.register(Chat)

