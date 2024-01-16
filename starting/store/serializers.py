from rest_framework import serializers

from .models import Collection


class CollectionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    featured_product=serializers.StringRelatedField()
    

class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    unit_price=serializers.DecimalField(max_digits=6, decimal_places=2)
    description=serializers.CharField()
    # () is function here
    collection=CollectionSerializer()
