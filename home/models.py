from django.db import models
from datetime import datetime



class Detail(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='images')
    date = models.DateTimeField(
        default=datetime.now, blank=True)

    def __str__(self):
        return self.title

