from tkinter import Widget
from django import forms
from .models import Detail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DetailForm(forms.ModelForm):

    class Meta:
        model = Detail
        fields = ('title', 'image')
     
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1', 'password2']