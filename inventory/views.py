from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from accounts.models import Accounts
from .models import *
from .forms import *


# Create your views here.


@login_required(login_url='log_in')
def add_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = Accounts.objects.create_user(
                    username=username, password=password,
                    email=email, is_supplier=True
                )
                Supplier.objects.create(user=user, name=name, address=address)
                return redirect('supplier_list')
    context = {
        'forms': forms
    }
    return render(request, 'inventory/add_supplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'inventory/supplier_list.html'
    context_object_name = 'supplier'


@login_required(login_url='log_in')
def add_customer(request):
    forms = CustomerForm()
    if request.method == 'POST':
        forms = CustomerForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = Accounts.objects.create_user(
                    username=username, password=password,
                    email=email, is_customer=True
                )
                Customer.objects.create(user=user, name=name, address=address)
                return redirect('customer_list')
    context = {
        'forms': forms
    }
    return render(request, 'inventory/add_customer.html', context)


class CustomerListView(ListView):
    model = Customer
    template_name = 'inventory/customer_list.html'
    context_object_name = 'customer'


@login_required(login_url='log_in')
def add_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product_list')
    context = {
        'forms': forms
    }
    return render(request, 'inventory/add_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'product'


@login_required(login_url='log_in')
def add_category(request):
    forms = CategoryForm()
    if request.method == 'POST':
        forms = CategoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('category_list')
    context = {
        'forms': forms
    }
    return render(request, 'inventory/add_category.html', context)


class CategoryListView(ListView):
    model = Category
    template_name = 'inventory/category_list.html'
    context_object_name = 'category'


@login_required(login_url='log_in')
def add_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            customer = forms.cleaned_data['customer']
            product = forms.cleaned_data['product']
            quantity = forms.cleaned_data['quantity']
            status = forms.cleaned_data['status']

            Order.objects.create(
                product=product,
                customer=customer,
                quantity=quantity,
                status=status,
            )
            return redirect('order_list')
    context = {
        'forms': forms
    }
    return render(request, 'inventory/add_order.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'inventory/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context


@login_required(login_url='log_in')
def edit_product(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        forms = ProductForm(instance=item)

        return render(request, 'inventory/edit_product.html', {'forms': forms})


@login_required(login_url='log_in')
def edit_category(request, pk):
    item = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        forms = CategoryForm(instance=item)

        return render(request, 'inventory/edit_category.html', {'forms': forms})


@login_required(login_url='log_in')
def edit_supplier(request, pk):
    item = get_object_or_404(Supplier, pk=pk)

    if request.method == "POST":
        form = SupplierForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        forms = SupplierForm(instance=item)

        return render(request, 'inventory/edit_supplier.html', {'forms': forms})


@login_required(login_url='log_in')
def edit_customer(request, pk):
    item = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        forms = CustomerForm(instance=item)

        return render(request, 'inventory/edit_customer.html', {'forms': forms})


@login_required(login_url='log_in')
def edit_order(request, pk):
    item = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        forms = OrderForm(instance=item)

        return render(request, 'inventory/edit_order.html', {'forms': forms})


@login_required(login_url='log_in')
def delete_product(request, pk):
    Product.objects.filter(id=pk).delete()
    forms = Product.objects.all()
    context = {
        'forms': forms,
    }

    return render(request, 'inventory/product_list.html', context)


@login_required(login_url='log_in')
def delete_category(request, pk):
    Category.objects.filter(id=pk).delete()
    forms = Category.objects.all()
    context = {
        'forms': forms,
    }

    return render(request, 'inventory/category_list.html', context)


@login_required(login_url='log_in')
def delete_order(request, pk):
    Order.objects.filter(id=pk).delete()
    forms = Order.objects.all()
    context = {
        'forms': forms,
    }

    return render(request, 'inventory/order_list.html', context)
