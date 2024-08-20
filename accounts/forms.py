from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
       
        
    def __init__(self, *args, **kwargs ):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'


        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-tr-3xl rounded-bl-3xl focus:border-sky-400 focus:ring-sky-300 focus:ring-opacity-40 focus:outline-none focus:ring'
