from django.urls import path

from . import views


urlpatterns = [
    path('records/', views.RecordListView.as_view(), name='records'),
    path('test/', views.test),
]
