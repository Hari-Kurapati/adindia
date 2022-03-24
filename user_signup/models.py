from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=30)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)