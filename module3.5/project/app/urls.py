from django.urls import path
from . import views


urlpatterns = [
    path('regions/', views.Region.as_view()),
]
