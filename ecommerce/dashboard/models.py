from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True,default='-')
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    county = models.CharField(max_length=30)

