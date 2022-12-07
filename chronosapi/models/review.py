from django.db import models


class Review(models.Model):
    review = models.CharField(max_length=500)
    customerId = models.ForeignKey("Customer", on_delete=models.CASCADE)
    watchId = models.ForeignKey("Watch", on_delete=models.CASCADE)
