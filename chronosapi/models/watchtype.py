from django.db import models


class WatchType(models.Model):
    type = models.CharField(max_length=50)
