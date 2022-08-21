from django.urls import path

from . import views


urlpatterns = [
    path('', views.AccountView.as_view(), name='account'),
    path('login/', views.ProfileLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.ProfileLogoutView.as_view(), name='logout'),
    path('registation/', views.ProfileRegistrationView.as_view(), name='registation'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('history_order/', views.HistoryOrderView.as_view(), name='history_order'),
    path('history_review/', views.HistoryReviewView.as_view(), name='history_review'),
]
