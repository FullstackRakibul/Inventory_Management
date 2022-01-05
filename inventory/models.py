from django.db import models
from accounts.models import Accounts


# Create your models here.

class Supplier(models.Model):
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    status_choice = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Confirmed', 'Confirmed'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=status_choice, default='Pending')
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity}pcs of {self.product.name} : {self.order_date}'
