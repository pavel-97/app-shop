from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/order_by_date/', views.ProductListOrderByDateListView.as_view(), name='products_order_by_date'),
    path('products/order_by_price/', views.ProductListOrderByPriceListView.as_view(), name='products_order_by_price'),
    path('products/order_by_views/', views.ProductListOrderByViewsListView.as_view(), name='products_order_by_views'),
    path('categories/<str:slug>/', views.CategoryView.as_view(), name='category'),
    path('categories/<str:slug>/order_by_views/', views.CategoryView.as_view(), name='category_order_by_views'),
    path('categories/<str:slug>/order_by_price/', views.CategoryOrderByPriceView.as_view(), name='category_order_by_price'),
    path('categories/<str:slug>/order_by_date/', views.CategoryOrderByDateView.as_view(), name='category_order_by_date'),
    path('basket/', views.BasketView.as_view(), name='basket'),
    path('add_product_in_basket/<str:slug>/', views.AddProductInBasketView.as_view(), name='add_product_in_basket'),
    path('delete_product_from_basket/<str:slug>/', views.DeleteProductFromBasket.as_view(), name='dalete_product_from_basket'),
    path('make_order/', views.MakeOrder.as_view(), name='make_order'),
    path('<str:slug>/', views.ProductDetailView.as_view(), name='product'),
]
