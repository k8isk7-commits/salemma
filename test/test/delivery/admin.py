from django.contrib import admin
from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'recipient_full_name', 'delivery_destination', 'contact_number', 'shipment_status']
    list_display_links = ['tracking_number', 'recipient_full_name']

admin.site.register(Delivery, DeliveryAdmin)
