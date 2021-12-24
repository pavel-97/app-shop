from django.urls import path
from . import views


urlpatterns = [
    path('advertisements/', views.AdvertisementListView.as_view()),
    path('advertisements/new_advertisement/', views.AdvertisementFormView.as_view()),
    path('advertisements/<int:pk>/', views.AdvertisementDetailView.as_view()),
]
