from django.db import models


# Create your models here.


class checkpoint(models.Model):
    checkpoint_id = models.CharField(primary_key=True, max_length=30)
    gps_x = models.FloatField(default=0.0)
    gps_y = models.FloatField(default=0.0)
    approval_status = models.BooleanField()
