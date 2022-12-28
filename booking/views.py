from django.shortcuts import render, redirect
from .forms import CreateBooking, CreateUserForm
from .models import Booking
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
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


