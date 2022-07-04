from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from . import models


class LoginForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input'})
        self.fields['password'].widget.attrs.update({'class': 'form-input'})
        

class ProfileRegistrationForm(UserCreationForm):
    
    def save(self, request, *args, **kwargs):
        user = super().save(*args, **kwargs)
        profile = models.Profile.objects.create(user=user)
        return self.login(request)
    
    def login(self, request):
        user = authenticate(request, username=self.cleaned_data['username'], password=self.cleaned_data['password2'])
        login(request, user)
        return redirect('profile')
        
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']