from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['item_title', 'unit_cost', 'stock_quantity']
    list_display_links = ['item_title']

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'product', 'quantity', 'created_at']
    list_display_links = ['id', 'customer_name']

admin.site.register(Order, OrderAdmin)