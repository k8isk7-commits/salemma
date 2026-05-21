from django.shortcuts import render, redirect, get_object_or_404
from .models import Delivery
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse

class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

class SimpleUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # إزالة جميع النصوص المساعدة (Help text) من الحقول
        for field in self.fields.values():
            field.help_text = ''

# Registration View
def register(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('delivery_index')
    else:
        form = SimpleUserCreationForm()
    return render(request, 'delivery/register.html', {'form': form})

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import DeliverySerializer

# API View (إرجاع البيانات بصيغة JSON ودعم إنشاء شحنات جديدة)
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def delivery_api(request):
    if request.method == 'GET':
        # جلب جميع البيانات من قاعدة البيانات
        deliveries = Delivery.objects.all().order_by('-id')
        serializer = DeliverySerializer(deliveries, many=True)
        # إرجاع البيانات بصيغة JSON
        return Response({'deliveries': serializer.data})
        
    elif request.method == 'POST':
        # استقبال البيانات من فلاتر وتخزينها
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ==========================================
# Class-Based Views (النسخة الجديدة بالكلاسات)
# ==========================================

class DeliveryListView(ListView):
    model = Delivery
    template_name = 'delivery/index.html'
    context_object_name = 'deliveries'

class DeliveryCreateView(LoginRequiredMixin, CreateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'delivery/form.html'
    success_url = reverse_lazy('delivery_index')

class DeliveryUpdateView(LoginRequiredMixin, UpdateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'delivery/form.html'
    success_url = reverse_lazy('delivery_index')
    # By default, CreateView and UpdateView look for <app>/<model>_form.html but we specified template_name

class DeliveryDeleteView(LoginRequiredMixin, DeleteView):
    model = Delivery
    template_name = 'delivery/delete.html'
    success_url = reverse_lazy('delivery_index')

# ==========================================
# Function-Based Views (الدوال القديمة - كتعليق)
# ==========================================
"""
def index(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/index.html', {'deliveries': deliveries})

def add_delivery(request):
    form = DeliveryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('delivery_index')
    return render(request, 'delivery/form.html', {'form': form})

def update_delivery(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    form = DeliveryForm(request.POST or None, instance=delivery)
    if form.is_valid():
        form.save()
        return redirect('delivery_index')
    return render(request, 'delivery/form.html', {'form': form})

def delete_delivery(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    if request.method == 'POST':
        delivery.delete()
        return redirect('delivery_index')
    return render(request, 'delivery/delete.html')
"""