from django.db import models
from .sendMail import sendMail
# Create your models here.
STATUS_PRODUCT = (
    (0, 'Ẩn'),
    (1, 'Công khai')
)


STATUS_ORDER = (
    (0, 'Chờ xác nhận'),
    (1, 'Đang giao'),
    (2, 'Đã giao')
)


class ProductCategory(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products_category')
    desc = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    price_discount = models.FloatField(default=0)
    discount = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_PRODUCT, default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images_product')
    image = models.ImageField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Hình ảnh {self.name} của {self.product.name}"


class ProductSize(models.Model):
    size = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.size


class ProductAttribute(models.Model):
    product_sku = models.CharField(max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes_product')
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, related_name='attribute_size')
    product_price = models.FloatField()
    product_discount = models.BooleanField(default=False)
    product_price_discount = models.FloatField(default=0)

    def __str__(self):
        return f"Sản phẩm {self.product.name} loại: {self.product_size}, giá: {self.product_price}"


class TimeFrameReceive(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    time_frame_receive = models.ForeignKey(TimeFrameReceive, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField(default=0, null=True, blank=True)
    province = models.CharField(max_length=20, null=True, blank=True)
    districts = models.CharField(max_length=20, null=True, blank=True)
    wards = models.CharField(max_length=20, null=True, blank=True)
    specific_address = models.CharField(max_length=50, null=True, blank=True)
    note = models.CharField(max_length=50, null=True, blank=True)
    customer_phone = models.CharField(max_length=11, null=True, blank=True)
    customer_name = models.CharField(max_length=50, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_ORDER, default=0)
    
    def get_total_amount(self):
        items = self.orders_detail.all()
        price = 0
        for item in items:
            price += item.get_total_price()
        
        self.amount = price
        self.save()

        return price
    
    def __str__(self):
        return f"Đơn hàng thứ {self.id} ngày {self.created}, tổng tiền: {self.get_total_amount()}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders_detail')
    product_attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, related_name='products_detail')
    quantity = models.IntegerField(default=1)

    def get_order_id(self):
        return self.order.id

    def get_product_name(self):
        return self.product_attribute.product.name
    
    def get_product_price(self):
        return self.product_attribute.product_price
    
    def get_product_price_discount(self):
        return self.product_attribute.product_price_discount

    def get_product_discount(self):
        return self.product_attribute.product_discount

    def get_product_sku(self):
        return self.product_attribute.product_sku
    
    def get_total_price(self):
        if self.get_product_discount():
            return self.quantity * self.get_product_price_discount()
        else:
            return self.quantity * self.get_product_price()
    
    def save(self, *args, **kwargs):
        super(OrderDetail, self).save(*args, **kwargs)
        order = self.order.get_total_amount()
        del order

    def __str__(self):
        return f"Đơn hàng {self.get_order_id()}, sản phẩm: {self.get_product_name()}, số lượng: {self.quantity}, tổng tiền: {self.get_total_price()}"
