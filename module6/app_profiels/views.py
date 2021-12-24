from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from . import forms
from . import models

# Create your views here.


class UserFormView(View):
    def get(self, request):
        user_form = forms.UserForm()
        return render(request, 'app_profiels/register.html', {'user_form': user_form, })
    
    def post(self, request):
        user_form = forms.UserForm(request.POST)

        if user_form.is_valid():
            models.User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'app_profiels/register.html', {'user_form': user_form})