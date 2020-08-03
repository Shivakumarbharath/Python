from django.db import models


class Catalog(models.Model):
    product_id = models.CharField(primary_key=True, max_length=40)
    product_name = models.TextField()
    product_price = models.IntegerField()

# Create your models here.
