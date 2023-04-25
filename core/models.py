from django.db import models

# Create your models here.
class song(models.Model):

    name = models.CharField(max_length=200)
    duration = models.IntegerField("la duration")
    lyrics = models.TextField('lyrics')
    
def __str__(self):
    return self.name

