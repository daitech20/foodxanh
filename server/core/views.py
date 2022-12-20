from django.shortcuts import render
from .serializers import OrderSerializer, ProductSerializer, OrderDetailSerializer, OrderDetailUpdateSerializer
from .models import Order, Product, OrderDetail
from rest_framework import generics, status


# Create your views here.
class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order
    serializer_class = OrderSerializer
    lookup_field = 'id'


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail
    serializer_class = OrderDetailSerializer
    lookup_field = 'id'


class OrderDetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail
    serializer_class = OrderDetailUpdateSerializer
    lookup_field = 'id'


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer
    lookup_field = 'id'


def index(request):
    return render(request, 'index.html')