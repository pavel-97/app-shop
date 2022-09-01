from django.urls import path

from . import api


urlpatterns = [
    path('list/', api.StockListAPIView.as_view()),
    path('list/<int:pk>/', api.StockRetrieveApiView.as_view()),
]
