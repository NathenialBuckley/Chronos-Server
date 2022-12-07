from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    address = models.CharField(max_length=155)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postalCode = models.IntegerField(max_length=5)
    phone = models.IntegerField(max_length=11)
    userId = models.ForeignKey("User", on_delete=models.CASCADE)
