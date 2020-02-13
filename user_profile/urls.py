from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_new_users, name='register_user'),
    path('home/', home, name='home'),
]
