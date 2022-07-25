from django.db import models
from datetime import datetime




class Detail(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(max_length=200,null=True,blank=True)
    date = models.DateTimeField( default=datetime.now, blank=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True)
    completion = models.BooleanField(default=True)

    def __str__(self):
        return self.title

