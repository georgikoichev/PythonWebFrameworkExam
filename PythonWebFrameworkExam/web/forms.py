from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Thread, Profile
from .validators import validate_nonzero, validate_non_negative


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Profile
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
            ),
        }


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class CalculatorForm(forms.Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField(validators=[validate_nonzero], required=True)
    operation = forms.ChoiceField(choices=[
        ('add', 'Add'),
        ('subtract', 'Subtract'),
        ('multiply', 'Multiply'),
        ('divide', 'Divide'),
        ('power', 'Power'),
    ])


class MathFunctionsForm(forms.Form):
    num = forms.FloatField(validators=[validate_non_negative], required=True)
    operation = forms.ChoiceField(choices=[
        ('square root', 'Square root'),
        ('sinus', 'Sinus'),
        ('cosine', 'Cosine'),
        ('tangent', 'Tangent'),
        ('cotangent', 'Cotangent'),
    ])