from rest_framework import serializers
from .models import Person, OrderHeader, OrderItem

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        
class OrderHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHeader
        fields = '__all__'
    
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'