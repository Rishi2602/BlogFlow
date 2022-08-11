
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Detail(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(max_length=200,null=True,blank=True)
    date = models.DateTimeField( default=timezone.now, blank=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True)
    completion = models.BooleanField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null= True)
    ProfilePicture = models.FileField(upload_to='media')
    PhoneNumber = models.CharField(max_length=15)

    def __str__(self):
        return str(self.user)