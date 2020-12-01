from django.contrib import admin
from .models import Product, ProductSize, ProductColor, ProductServices


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'owner', 'quantity', 'timestamp']


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['size', 'active']


@admin.register(ProductColor)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['color', 'active']


@admin.register(ProductServices)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['service', 'active']
