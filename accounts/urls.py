from django.urls import path

from .views import *

urlpatterns = [
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),

    path('register_supplier', register_supplier, name='register_supplier'),
    path('register_customer', register_customer, name='register_customer'),
]
