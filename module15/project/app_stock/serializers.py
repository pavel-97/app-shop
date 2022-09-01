from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from . import models


class StockSerializer(ModelSerializer):
    class Meta:
        model = models.Stock
        fields = ['id', 'title', 'date_start', 'date_end', 'discount']
