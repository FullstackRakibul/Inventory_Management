from django import forms
from .models import *


class NewUserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))


class CustomerForm(NewUserForm):
    def __init__(self, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)


class SupplierForm(NewUserForm):
    def __init__(self, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control', 'id': 'category'
            }),
            'supplier': forms.Select(attrs={
                'class': 'form-control', 'id': 'supplier'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'price'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'quantity'
            }),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control', 'id': 'customer'
            }),
            'product': forms.Select(attrs={
                'class': 'form-control', 'id': 'product'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'quantity'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'customer'
            }),
        }
