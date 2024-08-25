from django.db import models

# Create your models here.
class Counter(models.Model):
    query= models.CharField(max_length=100)
    cal = models.IntegerField(default= 0)
    add=models.BooleanField(default=False)

    def __str__(self)->str:
        return self.query