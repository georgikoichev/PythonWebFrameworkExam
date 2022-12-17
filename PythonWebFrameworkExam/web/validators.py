from django import forms


def validate_nonzero(value):
    if value == 0:
        raise forms.ValidationError('Invalid Input')


def validate_non_negative(value):
    if value < 0:
        raise forms.ValidationError('Invalid Input')