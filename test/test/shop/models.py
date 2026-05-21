from django.db import models

class Product(models.Model):
    item_title = models.CharField(max_length=100, verbose_name="عنوان السلعة المعروضة")
    item_details = models.TextField(verbose_name="تفاصيل السلعة ومواصفاتها")
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="تكلفة الوحدة")
    stock_quantity = models.IntegerField(default=0, verbose_name="الكمية المتوفرة بالمخزن")

    def __str__(self):
        return self.item_title

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج المطلوب", related_name="orders")
    quantity = models.IntegerField(default=1, verbose_name="الكمية المطلوبة")
    customer_name = models.CharField(max_length=100, verbose_name="اسم المشتري")
    customer_phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")

    def __str__(self):
        return f"طلب لـ {self.customer_name} - {self.product.item_title}"