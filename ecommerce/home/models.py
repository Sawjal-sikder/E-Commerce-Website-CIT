from django.db import models

class Slider(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    title3 = models.CharField(max_length=255, blank=True, null=True)
    offer_descripts = models.CharField(max_length=255, blank=True, null=True)
    product_slug = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title1} {self.title2} {self.title3}'
