from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


class StockListAPIView(ListAPIView, CreateAPIView, GenericAPIView):
    """Doc text for StockListAPIView"""
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StockRetrieveApiView(RetrieveAPIView, UpdateAPIView, GenericAPIView):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request)
