from django.db import models


class WatchType(models.Model):
    type = models.CharField(max_length=50)
    watchId = models.ForeignKey("Watch", on_delete=models.CASCADE)
