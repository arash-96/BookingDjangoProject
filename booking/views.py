from django.shortcuts import render, redirect

from .decorators import unauthenticated_user
from .forms import CreateBooking, CreateUserForm, UpdateProfile
from .models import Booking
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    form = CreateBooking()
    context = {'form': form}
    return render(request, 'website/booking.html', context)


@login_required(login_url='login')
def contact(request):
    return render(request, 'website/contact.html')


@login_required(login_url='login')
def createBooking(request):
    # form = CreateBooking()
    form = CreateBooking(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data

            pc = Booking(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                contactNumber=cd['contactNumber'],
                email=cd['email'],
                date_time=cd['date_time'],
                user=request.user,
            )
            pc.save()
            messages.success(request, 'You booked an appointment!')
            return redirect('home')
        else:
            return redirect('home')

    context = {'form': form}
    return render(request, 'website/booking.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)


def MyBooking(request):
    bookings = Booking.objects.filter(user_id=request.user)
    context = {'bookings': bookings}
    return render(request, 'website/mybookings.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UpdateProfile(instance=request.user)
        args = {'form': form}
        return render(request, 'website/myAccount.html', args)







