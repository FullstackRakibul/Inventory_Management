from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView

from inventory.forms import SupplierForm, CustomerForm
from inventory.models import Supplier, Customer
from .forms import LoginForm

# Create your views here.
from .models import Accounts


def log_in(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    return render(request, 'accounts/login.html', {"form": form})


def log_out(request):
    logout(request)
    return redirect('log_in')


def register_supplier(request):
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
                return redirect('log_in')
    context = {
        'forms': forms
    }
    return render(request, 'accounts/register_supplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'inventory/supplier_list.html'
    context_object_name = 'supplier'


def register_customer(request):
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
                return redirect('log_in')
    context = {
        'forms': forms
    }
    return render(request, 'accounts/register_customer.html', context)


class CustomerListView(ListView):
    model = Customer
    template_name = 'inventory/customer_list.html'
    context_object_name = 'customer'
