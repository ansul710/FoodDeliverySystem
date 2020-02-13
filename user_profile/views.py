from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import UserProfiles


# Create your views here.
def home(request):
    return render(request,'users/home.html', {})


def register_new_users(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            if user.is_authenticated:
                return redirect('home')
    else:
        form = RegisterForm()

    context = { 'form': form }

    return render(request, 'users/register.html', context)
