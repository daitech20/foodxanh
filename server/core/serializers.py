from rest_framework import serializers
from .models import Order, ProductImage, Product, OrderDetail, ProductAttribute

class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    product_attribute = ProductAttributeSerializer()

    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderDetailUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ['quantity']


class OrderSerializer(serializers.ModelSerializer):
    orders_detail = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images_product = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'