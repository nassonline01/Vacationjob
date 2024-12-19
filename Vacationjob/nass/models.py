from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=15,default="user")
    email=models.EmailField(max_length=30,default='abc@gmail.com')
    phone=models.BigIntegerField(default=1123)
    birth_date =models.DateField(null=True)
    gender_choice =[('male','Male'),('female','Female'),('other','Other')] 
    gender = models.CharField(max_length=10,choices=gender_choice,default='other')
    qualification = models.CharField(max_length=50,default='Not Specified')
    address = models.CharField(max_length=100,default='Not Specified')
    landmark = models.CharField(max_length=50,default='Not Specified')
    pincode = models.IntegerField(default='100000')
    city = models.CharField(max_length=50,default='Not Specified') 
    state = models.CharField(max_length=50,default='Not Specified') 
    country = models.CharField(max_length=50,default='Not Specified') 
    hobby = models.CharField(max_length=50,default='Not Specified') 
    annual_income = models.IntegerField(default='100000')
    languages = models.CharField(max_length=100,default='Not Specified')
    about = models.CharField(max_length=200,default='Not Specified')
    images = models.ImageField(upload_to='User_Images/', null=True, blank=True, default='default-profile.png')
