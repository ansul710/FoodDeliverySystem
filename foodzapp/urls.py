from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', orderfood, name='order_food'),
    path('qty/', quantity, name='qty'),

]
