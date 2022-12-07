from django.db import models


class FavoriteWatch(models.Model):
    watchId = models.ForeignKey("Watch", on_delete=models.CASCADE)
    customerId = models.ForeignKey("Customer", on_delete=models.CASCADE)
