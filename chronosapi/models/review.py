from django.db import models


class Review(models.Model):
    review = models.CharField(max_length=500)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    watch = models.ForeignKey("Watch", on_delete=models.CASCADE)
