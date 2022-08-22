import email
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.core.exceptions import ValidationError

from . import models


class LoginForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input'})
        self.fields['password'].widget.attrs.update({'class': 'form-input'})
        

class ProfileRegistrationForm(UserCreationForm):
    
    def save(self, request, *args, **kwargs):
        user = super().save(*args, **kwargs)
        models.Profile.objects.create(user=user)
        return self.login(request)
    
    def login(self, request):
        user = authenticate(request, username=self.cleaned_data['username'], password=self.cleaned_data['password2'])
        login(request, user)
        return redirect('profile')
        
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
        
        
class ChangeProfileForm(forms.ModelForm):
    avatar = forms.FileField(widget=forms.FileInput({'class': 'Profile-file form-input',
                'id': 'avatar',
                'data-validate': 'onlyImgAvatar',
                'name': 'avatar',
                'type': 'file',}), required=False)
        
    class Meta:
        model = models.Profile
        fields = ('avatar', 'telephon_number', )
        widgets = {
            'telephon_number': forms.TextInput(attrs={
                'class': 'form-input',
                'id': 'phone',
                'name': 'phone',
                'type': 'text',
                }),
        }
        

class ChangeUserForm(forms.ModelForm):
    
    first_last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-input',
        'id':'name',
        'name':'name',
        'type':'text',
        'value': '',
    }), required=False)
    
    new_password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'id': 'password',
        'name':  'password',
        'type': 'password',
        'placeholder': 'Тут можно изменить пароль',
    }), required=False)
    
    repeat_new_password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'id': 'password',
        'name':  'password',
        'type': 'password',
        'placeholder': 'Повторите новый пароль',
    }), required=False)
    
    def change_mail(self, request):
        user = request.user
        if self.cleaned_data.get('email'): User.objects.filter(pk=request.user.pk).update(email=self.cleaned_data.get('email'))
        return None
        
    def change_first_last_name(self, request):
        user = request.user
        first_name, last_name = self.cleaned_data.get('first_last_name').split() if self.cleaned_data.get('first_last_name') else (None, None)
        if first_name and last_name:
                user.first_name = first_name
                user.last_name = last_name
                return user.save()
        return None
    
    def change_password(self, request):
        password, password_1 = self.cleaned_data.get('new_password'), self.cleaned_data.get('repeat_new_password')
        if (password == password_1) and (password and password_1) is True:
            user = request.user
            user.set_password(password)
            return user.save()
        return None
                
    def save(self, request, *args, **kwargs):
        self.change_mail(request)
        self.change_first_last_name(request)
        self.change_password(request)
        return None
    
    def clean_password(self):
        password, password_1 = self.cleaned_data.get('new_password'), self.cleaned_data.get('repeat_new_password')
        if (password == password_1) and (password and password_1) is not None:
            return password
        raise ValidationError('Input password and repeat password fields')
        
    def clean_first_last_name(self):
        first_last_name = self.cleaned_data.get('first_last_name')
        try:
            first_name, last_name = first_last_name.split() if first_last_name else (None, None)
        except ValueError:
            raise ValidationError('Input first name and last name')
        return first_last_name
    
    class Meta:
        model = User
        fields = ('email', )
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-input',
                'id': 'mail',
                'name': 'mail',
                'type': 'text',
                }),
        }