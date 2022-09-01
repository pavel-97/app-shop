from rest_framework import serializers

from . import models

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ['id', 'name', 'description', 'weight']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name']