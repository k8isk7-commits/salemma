from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, OrderSerializer


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})


@login_required
def add_customer(request):

    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'shop/form.html', {'form': form})


@login_required
def update_customer(request, id):

    product = get_object_or_404(Product, id=id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'shop/form.html', {'form': form})


@login_required
def delete_customer(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('index')

    return render(request, 'shop/delete.html', {'product': product})


# API View (إرجاع البيانات بصيغة JSON بالتنسيق المطابق لتطبيق delivery)
def shop_api(request):
    # جلب جميع المنتجات والطلبات من قاعدة البيانات
    products = list(Product.objects.values())
    orders = list(Order.objects.values())
    # إرجاع البيانات بصيغة JSON
    return JsonResponse({
        'products': products,
        'orders': orders
    }, safe=False)
