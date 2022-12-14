from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Thread


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['thread_title', 'thread_text']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']