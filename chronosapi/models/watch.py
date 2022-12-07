from django.db import models


class Watch(models.Model):
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    customerId = models.ForeignKey("Customer", on_delete=models.CASCADE)
