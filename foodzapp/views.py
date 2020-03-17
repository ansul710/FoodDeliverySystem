from django.shortcuts import render, redirect
from .models import Items
from .forms import QuantityForm


# Create your views here.
def orderfood(request):
    data = Items.objects.all()
    context = {'products': data}
    return render(request, 'orders/order_food.html', context)


def createpost(request):
    if request.method == 'POST':
        if request.POST.get('qty'):
            items = Items()
            items.qty = request.POST.get('qty')
            items.save()
            context = {'qty': items.qty}
            return render(request, 'orders/qty.html', context)

    else:
        return render(request, 'orders/order_food.html', {})


def quantity(request):
    item = Items.objects.get(qty=request.method.POST)
    form = QuantityForm(data=request.POST or None)
    if form.is_valid():
        item.save()
        form.save()
        return render(request, 'orders/order_food.html', {})
    else:
        return render(request, 'orders/order_food.html', {})
