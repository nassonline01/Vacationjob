from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    phone=models.BigIntegerField(default=1010101010)
    birth_date =models.DateField(null=True)
    gender_choice =[('male','Male'),('female','Female'),('other','Other')] 
    gender = models.CharField(max_length=10,choices=gender_choice)
    status_choice =[('worker','Worker'),('student','Student'),('other','Other')]
    status = models.CharField(max_length=10,choices=status_choice)
    qualification = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    landmark = models.CharField(max_length=50)
    pincode = models.IntegerField(default=0)
    city = models.CharField(max_length=50) 
    state = models.CharField(max_length=50) 
    country = models.CharField(max_length=50) 
    hobby = models.CharField(max_length=50) 
    annual_income = models.IntegerField(default=0)
    languages = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    images = models.ImageField(upload_to='User_Images/')