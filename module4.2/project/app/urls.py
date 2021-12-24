from django.urls import path
from . import views


urlpatterns = [
    path('', views.Advertisement.as_view()),
]
