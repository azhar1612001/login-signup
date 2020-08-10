from django.db import models

# Create your models here.
class Detail(models.Model):
    username=models.CharField(max_length=50)
    add1=models.CharField(max_length=100)
    add2=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    occupation=models.CharField(max_length=100)
    pin=models.IntegerField()

    def __str__(self):
        return self.username
