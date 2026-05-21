from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.DeliveryListView.as_view(), name='delivery_index'),
    path('add/', views.DeliveryCreateView.as_view(), name='add_delivery'),
    path('update/<int:pk>/', views.DeliveryUpdateView.as_view(), name='update_delivery'),
    path('delete/<int:pk>/', views.DeliveryDeleteView.as_view(), name='delete_delivery'),
    
    # API
    path('api/', views.delivery_api, name='delivery_api'),
    
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]