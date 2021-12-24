from django.urls import path
from . import views


urlpatterns = [
    path("", views.advertisement_list, name='advertisements_list'),
    path("advertisement/", views.advertisement_detail, name='advertisement_detail'),
]
