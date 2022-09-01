from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin

from . import entities
from . import serializers
from . import models

# Create your views here.


class ItemListView(APIView):
    def get(self, request):
        items = models.Item.objects.all()
        serializer = serializers.ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


# class ItemDetailView(APIView):
#     def get(self, request, pk):
#         item = models.Item.objects.get(pk=pk)
#         serializer = serializers.ItemSerializer(item)
#         return Response(serializer.data)


class ItemDetailView(RetrieveModelMixin, GenericAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk)