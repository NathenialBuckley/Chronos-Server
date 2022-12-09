from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    address = models.CharField(max_length=155)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postalCode = models.IntegerField
    phone = models.IntegerField
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
