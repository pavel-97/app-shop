from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.core.cache import cache

from app_shop.utility import BasketContextMixin ,View, CategoryContextMixin
from app_shop.models import Product

from . import models
from . import forms

# Create your views here.


class AccountView(LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, View):
    template_name = 'app_profile/account.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile'] = models.Profile.objects.get(user=self.request.user)
        return context
    
    
class ProfileView(LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, UpdateView, View):
    model = models.Profile
    form_class = forms.ChangeProfileForm
    form_user = forms.ChangeUserForm
    template_name = 'app_profile/profile.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form_class(instance=self.request.user.profile)
        context['form_user'] = self.form_user(instance=self.request.user)
        return context
    
    def get_object(self):
        return self.model.objects.get(user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('account')
    
    def post(self, request, *args, **kwargs):
        form_user = self.form_user(request.POST)
        if form_user.is_valid():
            form_user.save(request)
        return super().post(request, *args, **kwargs)
        
        
class HistoryOrderView(LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, View):
    template_name = 'app_profile/history_order.html'
    model = models.HistoryOrder
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['history_order'] = self.model.objects.get(profile=self.request.user.profile)
        return context
    
    
class HistoryReviewView(LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, View):
    template_name = 'app_profile/history_review.html'
    
    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        review = cache.get('review', list())
        context['review'] = Product.objects.filter(pk__in=[product.pk for product in review]).prefetch_related('tag').prefetch_related('images')
        return context
    
    
class ProfileLoginView(BasketContextMixin, CategoryContextMixin, LoginView):
    template_name = 'app_profile/login.html'
    authentication_form = forms.LoginForm
    
    
class ProfileLogoutView(LogoutView):
    pass
    
    
class ProfileRegistrationView(BasketContextMixin, CategoryContextMixin, View):
    template_name = 'app_profile/registration.html'
    form = forms.ProfileRegistrationForm
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form()
        return context
    
    def post(self, request):
        form = forms.ProfileRegistrationForm(request.POST)
        context = dict(form=form,)
        if form.is_valid():
            return form.save(request)
        return render(request, 'app_profile/registration.html', context)
    