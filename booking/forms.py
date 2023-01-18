from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Booking


class CreateBooking(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    contactNumber = forms.IntegerField()
    email = forms.CharField(max_length=200)
    date_time = forms.DateTimeField()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfile(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']












