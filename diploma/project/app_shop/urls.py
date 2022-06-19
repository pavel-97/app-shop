from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('<str:slug>/', views.ProductDetailView.as_view(), name='product'),
]
