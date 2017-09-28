from django import forms
from django.core import validators
from django.forms import ModelForm

from new_app.models import User

class AddUser(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
