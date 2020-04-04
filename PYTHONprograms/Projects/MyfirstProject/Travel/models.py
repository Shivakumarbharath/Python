from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='Tpics')#all images are uploaede
    desc = models.TextField()
    offer = models.BooleanField(default=False)

