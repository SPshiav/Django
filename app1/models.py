from django.db import models

# Create your models here.
class train_details(models.Model):
    train_num=models.PositiveIntegerField(primary_key=True)
    train_name = models.CharField(max_length=260, unique=True)
    origin_city=models.CharField(max_length=260)
    destination_city=models.CharField(max_length=260)
    departure_time=models.TimeField()
    arrivaal_time=models.TimeField()
