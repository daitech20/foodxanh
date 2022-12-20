from django.contrib import admin
from .models import Product, ProductCategory, ProductAttribute, ProductImage, Order, OrderDetail, TimeFrameReceive, ProductSize
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductAttribute)
admin.site.register(ProductCategory)
admin.site.register(ProductSize)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(TimeFrameReceive)
