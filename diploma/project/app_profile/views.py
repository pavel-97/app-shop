from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from . import models
from . import forms

# Create your views here.


class AccountView(LoginRequiredMixin, View):
    def get(self, request):
        profile = models.Profile.objects.get(user=request.user)
        context = dict(profile=profile)
        return render(request, 'app_profile/account.html', context)
    
    
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'app_profile/profile.html')
    
    
class HistoryOrderView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'app_profile/history_order.html')
    
    
class ProfileLoginView(LoginView):
    template_name = 'app_profile/login.html'
    authentication_form = forms.LoginForm
    
    
class ProfileRegistrationView(View):
    def get(self, request):
        form = forms.ProfileRegistrationForm()
        context = dict(form=form,)
        return render(request, 'app_profile/registration.html', context)
    
    def post(self, request):
        form = forms.ProfileRegistrationForm(request.POST)
        context = dict(form=form,)
        if form.is_valid():
            return form.save(request)
        return render(request, 'app_profile/registration.html', context)