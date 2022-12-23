from django.shortcuts import render
from .serializers import OrderSerializer, ProductSerializer, OrderDetailSerializer, OrderDetailUpdateSerializer
from .models import Order, Product, OrderDetail, ProductCategory, ProductImage
from rest_framework import generics, status
from django import template

register = template.Library()

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
    data = {
        "product_categories": ProductCategory.objects.all(),
        "products": Product.objects.all(),
        "product_images": ProductImage.objects.all()
    }

    return render(request, 'index.html', data)