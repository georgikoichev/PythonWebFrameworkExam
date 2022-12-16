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
        widgets = {
            'thread_title': forms.TextInput(
                attrs={
                    'placeholder': 'Thread Name',
                }
            ),
            'thread_text': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                },
            )
        }


class DeleteThreadForm(CreateThreadForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']