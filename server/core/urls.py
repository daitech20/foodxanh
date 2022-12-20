from django.urls import path, include
from .views import OrderView, ProductList, ProductDetail, OrderDetailView, OrderDetailUpdateView, index


urlpatterns = [
    path('', index, name='index'),
    path('api/order/<int:id>', OrderView.as_view(), name='order_view'),
    path('api/orderdetail/<int:id>', OrderDetailView.as_view(), name='order_detail_view'),
    path('api/orderdetail/update/<int:id>', OrderDetailUpdateView.as_view(), name='order_detail_update_view'),
    path('api/products', ProductList.as_view(), name='product_list'),
    path('api/product/<int:id>', ProductDetail.as_view(), name='product_detail'),
]
