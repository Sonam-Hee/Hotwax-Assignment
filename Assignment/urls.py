"""
URL configuration for Assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Assignment/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hotwax.views import CreatePersonView, CreateOrderView, AddOrderItemsView, GetAllOrdersView, GetOrderView, UpdateOrderView


# router = routers.DefaultRouter()
# router.register(r'create-person', CreatePersonView, basename='create-person')
# router.register(r'create-order', CreateOrderView, basename='create-order')
# router.register(r'add-order-items', AddOrderItemsView, basename='add-order-items')
# router.register(r'get-all-orders', GetAllOrdersView, basename='get-all-orders')
# router.register(r'get-order', GetOrderView, basename='get-order')
# router.register(r'update-order', UpdateOrderView, basename='update-order')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotwax.urls')),
    
    # path('create-person/', CreatePersonView.as_view(), name='create-person'),
    # path('', include('router.urls')),  
]


# Alternate method


# urlpatterns = [
  
#     path('api/create-person/', CreatePersonView.as_view(), name='create-person'),

#     path('api/create-order/', CreateOrderView.as_view(), name='create-order'),

#     path('api/add-order-items/', AddOrderItemsView.as_view(), name='add-order-items'),

#     path('api/get-all-orders/', GetAllOrdersView.as_view(), name='get-all-orders'),

#     path('api/get-order/<str:pk>/', GetOrderView.as_view(), name='get-order'),

#     path('api/update-order/<str:pk>/', UpdateOrderView.as_view(), name='update-order'),

#     path('admin/', admin.site.urls),
# ]
