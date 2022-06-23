from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/order_by_date/', views.ProductListOrderByDateListView.as_view(), name='products_order_by_date'),
    path('products/order_by_price/', views.ProductListOrderByPriceListView.as_view(), name='products_order_by_price'),
    path('basket/', views.BasketView.as_view(), name='basket'),
    path('<str:slug>/', views.ProductDetailView.as_view(), name='product'),
]
