from django.db import models

# Create your models here.
class Documentes(models.Model):
    fileName = models.CharField(max_length=60)
    number = models.CharField(max_length=20)
    barcode = models.CharField(max_length=30)
    codeType = models.CharField(max_length=30)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
