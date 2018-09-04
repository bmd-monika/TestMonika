from django.db import models

class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fromRate = models.CharField(max_length=100, blank=True, default='')
    toRate = models.CharField(max_length=100, blank=True, default='')