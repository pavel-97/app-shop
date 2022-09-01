from django.urls import path

from . import views


urlpatterns = [
    path('<int:pk>/', views.NewsDetailView.as_view(), name='detail_news'),
    path('', views.news_list, name='news'),
]

