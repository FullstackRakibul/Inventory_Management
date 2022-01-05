from django.contrib import admin

# Register your models here.
from accounts.models import Accounts


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_customer', 'is_supplier']


admin.site.register(Accounts, UserAdmin)
