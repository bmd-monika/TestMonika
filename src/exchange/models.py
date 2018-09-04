from django.db import models
from src.rate.models import Rate
# Create your models here.
class Exchange(models.Model):
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE, max_length=50)
    date = models.DateTimeField(blank=True, null=True)
    value = models.FloatField(max_length=15)