from django.urls import path

from .views import *

urlpatterns = [
    path('add_customer', add_customer, name='add_customer'),
    path('add_supplier', add_supplier, name='add_supplier'),
    path('add_product', add_product, name='add_product'),
    path('add_order', add_order, name='add_order'),
    path('add_category', add_category, name='add_category'),

    # path('edit_customer/<pk>', edit_customer, name='edit_customer'),
    # path('edit_supplier/<pk>', edit_supplier, name='edit_supplier'),
    path('edit_product/<pk>', edit_product, name='edit_product'),
    path('edit_order/<pk>', edit_order, name='edit_order'),
    path('edit_category/<pk>', edit_category, name='edit_category'),

    # path('delete_customer/<pk>', delete_customer, name='delete_customer'),
    # path('delete_supplier/<pk>', delete_supplier, name='delete_supplier'),
    path('delete_product/<pk>', delete_product, name='delete_product'),
    path('delete_order/<pk>', delete_order, name='delete_order'),
    path('delete_category/<pk>', delete_category, name='delete_category'),

    path('customer_list', CustomerListView.as_view(), name='customer_list'),
    path('supplier_list', SupplierListView.as_view(), name='supplier_list'),
    path('product_list', ProductListView.as_view(), name='product_list'),
    path('order_list', OrderListView.as_view(), name='order_list'),
    path('category_list', CategoryListView.as_view(), name='category_list'),

]
