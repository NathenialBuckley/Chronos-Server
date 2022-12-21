from django.db import models


class Watch(models.Model):
    name = models.CharField(max_length=50)
    watchtype = models.ForeignKey(
        "WatchType", on_delete=models.CASCADE, related_name="watches")
    price = models.CharField(max_length=50)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    image = models.CharField(max_length=300)
