from django.urls import path

from . import views


urlpatterns = [
    path('', views.AccountView.as_view(), name='account'),
    path('login/', views.ProfileLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('registation/', views.ProfileRegistrationView.as_view(), name='registation'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('history_order/', views.HistoryOrderView.as_view(), name='history_order'),
]
