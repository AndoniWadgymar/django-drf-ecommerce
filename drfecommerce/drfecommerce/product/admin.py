from django.contrib import admin

from drfecommerce.product.models import Category, Brand, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)