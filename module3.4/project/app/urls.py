from django.urls import path
from . import views


urlpatterns = [
    path('contacts/', views.contacts),
    path('about/', views.about),
    path('categories/', views.categories),
    path('regions/', views.regions),
]
