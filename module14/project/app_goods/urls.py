from django.urls import path
from . import views


urlpatterns = [
    path('items/', views.ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='item_list'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
]
