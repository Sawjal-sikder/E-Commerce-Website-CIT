from django.db import models

# Create your models here.
class slider(models.Model):
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)
    title3 = models.CharField(max_length=50)
    offer_title = models.CharField(max_length=150)
    banar = models.ImageField(upload_to='slider_images/')

    def __str__(self):
        return f'{self.title1} {self.offer_title}'



class condation(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    thumbnil = models.ImageField(upload_to='condation_images/')

    def __str__(self):
        return f'{self.title}'

class offer(models.Model):
    title = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)
    title3 = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    banar = models.ImageField(upload_to='offer_images/')

    def __str__(self):
        return f'{self.title}-{self.title2} - {self.title3}'
