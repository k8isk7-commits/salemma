# pyrefly: ignore [missing-import]
from django.db import models

class Delivery(models.Model):
    SHIPMENT_STATUS_CHOICES = [
        ('Pending', 'قيد التحقق والاستلام'),
        ('Delivered', 'تم التوصيل للعميل'),
        ('Cancelled', 'ملغي من قبل الإدارة'),
    ]

    recipient_full_name = models.CharField(max_length=100, verbose_name="الاسم الكامل للمستلم")
    tracking_number = models.IntegerField(verbose_name="رقم التتبع للطلب")
    delivery_destination = models.CharField(max_length=200, verbose_name="وجهة التوصيل والمنطقة")
    contact_number = models.CharField(max_length=20, verbose_name="رقم التواصل الهاتفي")
    shipment_status = models.CharField(max_length=20, choices=SHIPMENT_STATUS_CHOICES, default='Pending', verbose_name="حالة الشحنة")

    def __str__(self):
        return f"شحنة #{self.tracking_number} - {self.recipient_full_name}"

