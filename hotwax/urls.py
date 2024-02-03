from django.urls import path, include
from . import views
from .views import CreatePersonView, CreateOrderView, AddOrderItemsView, GetAllOrdersView, GetOrderView, UpdateOrderView
from rest_framework import routers


# urlpatterns = [
#     # creating a person
#     path('create-person/', CreatePersonView.as_view(), name='create-person'),

#     # creating an order
#     path('create-order/', CreateOrderView.as_view(), name='create-order'),

#     # adding order items
#     path('add-order-items/', AddOrderItemsView.as_view(), name='add-order-items'),

#     # getting all orders
#     path('get-all-orders/', GetAllOrdersView.as_view(), name='get-all-orders'),

#     # getting a specific order
#     path('get-order/<str:pk>/', GetOrderView.as_view(), name='get-order'),

#     # updating an order
#     path('update-order/<str:pk>/', UpdateOrderView.as_view(), name='update-order'),
# ]


router = routers.DefaultRouter()
router.register(r'create-person', CreatePersonView, basename='create-person')
router.register(r'create-order', CreateOrderView, basename='create-order')
router.register(r'add-order-items', AddOrderItemsView, basename='add-order-items')
router.register(r'get-all-orders', GetAllOrdersView, basename='get-all-orders')
router.register(r'get-order', GetOrderView, basename='get-order')
router.register(r'update-order', UpdateOrderView, basename='update-order')

urlpatterns = [
    path('', include(router.urls))
]

