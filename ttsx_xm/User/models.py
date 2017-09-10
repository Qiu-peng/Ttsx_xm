from django.db import models

# Create your models here.
class UserInfo(models.Model):
    userName = models.CharField(max_length=20)
    userPsw = models.CharField(max_length=20)
    userEmail = models.CharField(max_length=30)
    isValid = models.BooleanField(default=True)
    isActive = models.BooleanField(default=False)