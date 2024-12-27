from django.shortcuts import render,redirect , HttpResponse , get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Register,BankDetails,Task,Wallet ,TaskUserAssignment
from django.contrib.auth.decorators import login_required
from .forms import TaskSubmissionForm
# Create your views here.
@never_cache
def index(request):
  return render(request,'index.html')
@never_cache
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Check if the user is an admin
            if user.is_superuser :
                return redirect('admin_dashboard')  # Redirect to admin dashboard
            
            # Otherwise, redirect to a general user dashboard or home
            return redirect('user_dashboard')
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

@never_cache
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        confirmpassword = request.POST.get('confirmpassword')
        
        # Check if passwords match
        if password != confirmpassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('register_view')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return redirect('register_view')

        # Create user
        user = User.objects.create_user(username=username, password=password)
        student = Register.objects.create(
            user=user,
            first_name=first_name, 
            email=email, 
            phone=phone
        )
        
        student.save()
        messages.success(request, 'Registration successful!')
        return HttpResponse("<script>window.alert('Registration successful!');window.location.href=('/login/');</script>")
    
    return render(request, 'signup.html')

def admin_dashboard(request):
    return render(request, 'Admin.html')

def user_dashboard(request):
    try:
        person = Register.objects.get(user=request.user)
    except:
        return HttpResponse("<script>window.alert('Problem with user');window.location.href=('/login/');</script>")
    return render(request, 'User.html',{'person':person})

def verify_dashboard(request):
    return render(request, 'verificationteam.html')

def profile_view(request):
    try:
        person = Register.objects.get(user=request.user)
    except:
        return HttpResponse("<script>window.alert('Problem with user');window.location.href=('/userprofile/');</script>")
    if request.method == 'POST':
        person.first_name = request.POST['name']
        person.email = request.POST['email']
        person.phone = request.POST['phone']
        person.birth_date = request.POST['dob']
        person.gender = request.POST['gender']
        person.status = request.POST['status']
        person.qualification = request.POST['qualification']
        person.address = request.POST['address']
        person.landmark = request.POST['land']
        person.pincode = request.POST['pin']
        person.country = request.POST['country']
        person.state = request.POST['state']
        person.city = request.POST['city']
        person.hobby = request.POST['hobby']
        person.languages = request.POST['language']
        person.annual_income = request.POST['annual']
        person.about = request.POST['about']
        person.images = request.FILES.get('profile_photo')
        person.save()
        return HttpResponse("<script>window.alert('Congrats...! your Profile has been Updated');window.location.href=('/user/');</script>")
    else:
        return render(request, 'Profile.html',{'Data':person})
    
def Logout(request):
    logout(request)
    return HttpResponse("<script>window.alert('Log Out Success');window.location.href=('/login/');</script>")

def Bank_Details(request):
    if request.method == 'POST': 
        user = User.objects.get(username=request.user)
        account_holder = request.POST['accountHolder']
        account_number = request.POST['accountNumber']
        ifsc_code = request.POST['ifscCode']
        bank_name = request.POST['bankName']
        bank_details = BankDetails.objects.create(
            user = user , account_holder =account_holder ,account_number=account_number,
            ifsc_code =ifsc_code,bank_name =bank_name
        )
        bank_details.save()
        return HttpResponse("<script>window.alert(' Bank Details saved');window.location.href=('/user/');</script>")
    else:
        return render(request, "User.html", {"bank_details": bank_details})

def Account(request):
    return render(request,'Account.html')

def dashboard(request):
    user = request.user
    tasks = Task.objects.filter(assigned_to=user)
    wallet, created = Wallet.objects.get_or_create(user=user)
    return render(request, 'dashboard.html', {'tasks': tasks, 'wallet': wallet})    

def JobList(request):
    # tasks = Task.objects.filter(assigned_to__isnull=True).order_by('deadline')  
    tasks = Task.objects.all()
    return render(request, 'joblist.html', {'tasks': tasks})

@login_required
def submit_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)
    user_assignment, created = TaskUserAssignment.objects.get_or_create(task=task,user=request.user)
    if request.method == 'POST':
        form = TaskSubmissionForm(request.POST, request.FILES, instance=user_assignment)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.actions = {
                'like': form.cleaned_data['like'],
                'subscribe': form.cleaned_data['subscribe'],
                'follow': form.cleaned_data['follow'],
                'comment': form.cleaned_data['comment']
            }
            submission.save()
            return  HttpResponse("<script>window.alert('Your Work Submitted Successfully');window.location.href=('/dashboard/');</script>")
    else:
        form = TaskSubmissionForm(instance=user_assignment)

    return render(request, 'submit_task.html', {'form': form, 'task': task})
