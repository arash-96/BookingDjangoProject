from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contactNumber = models.IntegerField()
    email = models.CharField(max_length=200, blank=False)
    date_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)




