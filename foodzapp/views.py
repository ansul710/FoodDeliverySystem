from django.shortcuts import render, redirect
from .models import Items


# Create your views here.
def orderfood(request):
    data = Items.objects.all()
    context = {'products': data}
    return render(request, 'orders/order_food.html', context)


