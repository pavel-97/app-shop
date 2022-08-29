from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
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
        

class ChangeUserForm(PasswordChangeForm, forms.ModelForm):
    email, first_name, last_name, old_password, new_password1, new_password2 = (
        forms.CharField(widget=forms.TextInput(attrs={
            'class': class_field,
            'id': id_field,
            'name': name_field,
            'type': type_field,
            'placeholder': placeholder_field,
            'value': value_field,
        }), required=False) for class_field, id_field, name_field, type_field, placeholder_field, value_field, in (
            ('form-input', 'mail', 'mail', 'text', '', ''),
            ('form-input', 'name', 'name', 'text', '', ''),
            ('form-input', 'name', 'name', 'text', '', ''),
            ('form-input', 'old_password', 'old_password', 'password', 'Введите старый пароль', ''),
            ('form-input', 'new_password1', 'new_password1', 'password', 'Тут можно изменить пароль', ''),
            ('form-input', 'new_password2', 'new_password2', 'password', 'Введите пароль повторно', '')
        )
    )
        
    def clean_old_password(self):
        old_password = self.data.get('old_password')
        if old_password == '': return ''
        return super().clean_old_password()
    
    def clean_new_password1(self):
        if self.data.get('new_password1') == '': return ''
        return self.data.get('new_password1')

    def clean_new_password2(self):
        if self.data.get('new_password2') == '': return ''
        return super().clean_new_password2()
    
    def save(self, request, commit=True):
        user = request.user
        user.email, user.first_name, user.user_last_name = (self.cleaned_data.get(key) for key in ('email', 'first_name', 'last_name'))
        old_password, new_password1, new_password2 = (self.data.get(key) for key in ('old_password', 'new_password1', 'new_password2'))
        user.save()
        if old_password == '' and new_password1 == '' and new_password2 == '': return None
        return super().save(commit)
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')