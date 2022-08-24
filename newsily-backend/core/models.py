from django.db import models

# Create your models here.

class StoreRequestInfoInEpoch(models.Model):
    """
    Store the request info in epoch time.
    """
    epoch_time = models.BigIntegerField()
    request_info = models.TextField()

    def __str__(self):
        return str(self.epoch_time)