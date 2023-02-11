from django.db import models

# Create your models here.
class fare(models.Model):
    trainnum = models.PositiveIntegerField()
    origincity = models.CharField(max_length=260)
    destinationcity = models.CharField(max_length=260)
    TrainFare = models.PositiveIntegerField()

