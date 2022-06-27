from turtle import title
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    special_price = models.IntegerField(null=True)
    is_premium = models.BooleanField(default=False)
    pmt_end = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    
    def __str__(self) -> str:
        return "{}".format(self.title)