from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Post, Comment, UserProfile


class UserForm(UserCreationForm):

    class Meta:
        fields = ("username", 'first_name', 'last_name', "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class UserEditForm(UserChangeForm):
    class Meta:
        fields=("username", "first_name","last_name", "email",)
        model = get_user_model()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_pic',)