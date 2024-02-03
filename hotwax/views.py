from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Person, OrderHeader, OrderItem
from .serializers import PersonSerializer,OrderHeaderSerializer, OrderItemSerializer
from rest_framework import viewsets


class CreatePersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class CreateOrderView(viewsets.ModelViewSet):
    queryset = OrderHeader.objects.all()
    serializer_class = OrderHeaderSerializer

class AddOrderItemsView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
class GetAllOrdersView(viewsets.ModelViewSet):
    queryset = OrderHeader.objects.all()
    serializer_class = OrderHeaderSerializer
    
class GetOrderView(viewsets.ModelViewSet):
    queryset = OrderHeader.objects.all()
    serializer_class = OrderHeaderSerializer

class UpdateOrderView(viewsets.ModelViewSet):
    queryset = OrderHeader.objects.all()
    serializer_class = OrderHeaderSerializer


# class CreatePersonView(generics.CreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class CreateOrderView(generics.CreateAPIView):
#     queryset = OrderHeader.objects.all()
#     serializer_class = OrderHeaderSerializer

# class AddOrderItemsView(generics.CreateAPIView):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
    
# class GetAllOrdersView(generics.ListAPIView):
#     queryset = OrderHeader.objects.all()
#     serializer_class = OrderHeaderSerializer
    
# class GetOrderView(generics.RetrieveAPIView):
#     queryset = OrderHeader.objects.all()
#     serializer_class = OrderHeaderSerializer

# class UpdateOrderView(generics.UpdateAPIView):
#     queryset = OrderHeader.objects.all()
#     serializer_class = OrderHeaderSerializer