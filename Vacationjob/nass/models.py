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

class BankDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    account_holder =models.CharField(max_length=50)
    account_number =models.CharField(max_length=20)
    ifsc_code =models.CharField(max_length=20)
    bank_name =models.CharField(max_length=50)
    branch =models.CharField(max_length=50)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    payout = models.DecimalField(max_digits=6, decimal_places=2)
    deadline = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')
    users_assigned = models.ManyToManyField(User, through='TaskUserAssignment', related_name='tasks_assigned')
    proof = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

class TaskUserAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_claimed = models.BooleanField(default=False)
    proof_submitted = models.BooleanField(default=False)
    clicked_at = models.DateTimeField(null=True, blank=True)
    proof_screenshot = models.ImageField(upload_to='task_proofs/screenshots/', blank=True, null=True)
    proof_video = models.FileField(upload_to='task_proofs/videos/', blank=True, null=True)
    proof_text = models.TextField(blank=True, null=True)
    actions = models.JSONField(default=dict)
    submission_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')], default='Pending')

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
