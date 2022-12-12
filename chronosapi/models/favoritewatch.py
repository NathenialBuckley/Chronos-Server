from django.db import models


class FavoriteWatch(models.Model):
    watch = models.ForeignKey("Watch", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
