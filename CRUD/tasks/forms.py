from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class RegistationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username", "password1", "password2")
