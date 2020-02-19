from django.db import models


# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=100, default=' ', null=True)
    item_desc = models.CharField(max_length=500, default=' ', null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    item_img = models.FileField(upload_to='image/', blank=True, null=True)
    # quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.item_name
