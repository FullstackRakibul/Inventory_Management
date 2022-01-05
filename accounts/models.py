from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Accounts(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
