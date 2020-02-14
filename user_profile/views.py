from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangePasswordForm, EditUserProfile
from .models import UserProfiles
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'users/home.html', {})


def register_new_users(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            object_usr = form.save(commit=False)
            object_usr.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            if user.is_authenticated:
                return redirect('home_page')
    else:
        form = RegisterForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully been logged in')
            return redirect('home_page')
        else:
            messages.success(request, 'Error logging in. Please try again!')
            return redirect('login_page')
    else:
        return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home_page')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST or None, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed Successfully')
            return redirect('login_page')
    else:
        form = ChangePasswordForm(user=request.user)
    context = {'form': form}
    return render(request, 'users/change_password.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserProfile(data=request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('home_page')
    else:
        form = EditUserProfile(instance=request.user)
        context = {'form': form}
        return render(request, 'users/user_profile.html', context)


