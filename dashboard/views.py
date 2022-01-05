from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from inventory.models import *


# Create your views here.
@login_required(login_url='log_in')
def dashboard(request):
    product_count = Product.objects.count()
    customer_count = Customer.objects.count()
    supplier_count = Supplier.objects.count()
    orders_count = Order.objects.count()
    orders = Order.objects.order_by('-id')
    context = {
        'product': product_count,
        'customers': customer_count,
        'supplier': supplier_count,
        'order': orders_count,
        'orders': orders,
    }
    return render(request, 'dashboard.html', context)
