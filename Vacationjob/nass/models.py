from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=15,default="user")
    email=models.EmailField(max_length=30,default='abc@gmail.com')
    phonenumber=models.BigIntegerField(default=1123)
    