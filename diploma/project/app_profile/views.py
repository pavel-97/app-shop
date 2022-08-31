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
    """
    Класс AccountView. Наследник классов LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, View.
    Реализует страницу аккаунта авторизированного пользователя.
    """
    template_name = 'app_profile/account.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile'] = models.Profile.objects.get(user=self.request.user)
        context['last_order'] = self.request.user.profile.order_set.latest('created_at')
        return context
    
    
class ProfileView(LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, UpdateView):
    """
    Класс ProfileView. Наследник классов LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, UpdateView.
    Реализует страницу изменения данных профиля авторизированного пользователя.
    """
    template_name = 'app_profile/profile.html'
    form_class = forms.ChangeProfileForm
    model = models.Profile
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form_user'] = forms.ChangeUserForm(self.request.user, initial={
            'email': self.request.user.email,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            })
        return context
        
    def get_object(self):
        return self.model.objects.get(user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('account')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_user = forms.ChangeUserForm(request.user, request.POST)
        if form_user.is_valid():
            form_user.save(request)
            return super().post(request, *args, **kwargs)
        return render(request, self.template_name, self.get_context_data()|{'form_user': form_user, })
    
    
class HistoryOrderView(LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, View):
    """
    Класс HistoryOrderView. Наследник классов LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, View.
    Реализует страницу вывода истории заказов авторизированного пользователя.
    """
    template_name = 'app_profile/history_order.html'
    model = models.HistoryOrder
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['history_order'] = self.model.objects.get(profile=self.request.user.profile)
        return context
    
    
class HistoryReviewView(LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, View):
    """
    Класс HistoryReviewView. Наследник классов LoginRequiredMixin, BasketContextMixin, CategoryContextMixin, View.
    Реализует страницу вывода истории просмотров товаров авторизированного пользователя.
    """
    template_name = 'app_profile/history_review.html'
    
    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        review = cache.get('review', list())
        context['review'] = Product.objects.filter(pk__in=[product.pk for product in review]).prefetch_related('tag').prefetch_related('images')
        return context
    
    
class ProfileLoginView(BasketContextMixin, CategoryContextMixin, LoginView):
    """
    Класс ProfileLoginView. Наследник классов BasketContextMixin, CategoryContextMixin, LoginView.
    Реализует страницу авторизации для неавторизированного пользователя.
    """
    template_name = 'app_profile/login.html'
    authentication_form = forms.LoginForm
    
    
class ProfileLogoutView(LogoutView):
    """
    Класс ProfileLogoutView. Наследник классов LogoutView.
    Класс реализует перенаправление для пользователя который вышел из своего аккаунта.
    """
    pass
    
    
class ProfileRegistrationView(BasketContextMixin, CategoryContextMixin, View):
    """
    Класс ProfileRegistrationView. Наследник классов BasketContextMixin, CategoryContextMixin, View.
    Реализует страницу регистрации неавторезированного пользователя, если у него еще нет аккаунта.
    """
    template_name = 'app_profile/registration.html'
    form = forms.ProfileRegistrationForm
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form()
        return context
    
    def post(self, request):
        form = forms.ProfileRegistrationForm(request.POST)
        if form.is_valid():
            return form.save(request)
        return render(request, 'app_profile/registration.html', self.get_context_data() | {'form': form, })
    