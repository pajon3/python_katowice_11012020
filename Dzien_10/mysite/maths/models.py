from django.db import models

# Create your models here.

class Math(models.Model):
    operation = models.CharField(max_length=10)
    a = models.IntegerField()
    b = models.IntegerField(blank=True, null = True)
    created = models.DateTimeField(auto_now_add=True)