from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(label="Enter product name")
    price = serializers.FloatField()
    description = serializers.CharField()
    count = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)
