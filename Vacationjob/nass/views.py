from django.shortcuts import render,redirect , HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Register


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
# @never_cache
# def Register(request):
#   return render(request,'signup.html')
# @never_cache
# def reg_view(request):
#     if request.method=='POST':
#         print("Form submitted")
#         name=request.POST['fristname']
#         email=request.POST['email']
#         username=request.POST['username']
#         password=request.POST['password']
#         phonenumber=request.POST['phonenumber']
#         # usertype = request.POST['usertype']
        
#         if Register.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken.")
#             return redirect('reg_view')

#         if Register.objects.filter(email=email).exists():
#             messages.error(request, "Email already registered.")
#             return redirect('reg_view')

#         user = Register.objects.create(
#             first_name=name,
#             email=email,
#             username=username,
#             password=password,
#             phonenumber=phonenumber
#             # usertype=usertype,
#             # is_approved=(usertype != 'authority')  # Auto-approve community users
#         )
#         user.save()
#         print("User created:", user)
# -----------------------------------------------

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
            # username=username, 
            first_name=first_name, 
            email=email, 
            phone=phone
            # password=password,  # Storing raw passwords in your model is insecure, consider removing this
            # confirmpassword=confirmpassword,  # Same as above
        )
        
        student.save()
        messages.success(request, 'Registration successful!')
        return redirect('login1')
    
    return render(request, 'signup.html')

        # if usertype == 'community':
        #     login(request, user)  # Log in the community user immediately
        #     return redirect("community_dashboard")
        #     # return redirect("community_dashboard")
        # elif usertype == 'authority':
        #     login(request, user)  # Log in the community user immediately
        #     return redirect("authority_dashboard")
        # else:
    #     return redirect('login.html')
    # else:
    #     return render(request,'signup.html')
def admin_dashboard(request):
    return render(request, 'Admin.html')

def user_dashboard(request):
    return render(request, 'User.html')
def verify_dashboard(request):
    return render(request, 'verificationteam.html')

def profile_view(request):
    try:
        person = Register.objects.get(user=request.user)
    except:
        return HttpResponse("<script>window.alert('Problem with user');window.href.location('/userprofile/');</script>")
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
        # person.images = request.FILES['images']

        # person = Register.objects.create(
        #     first_name = a , email = b , phone = c , birth_date = d , gender = e , qualification = f ,
        #     address = g , landmark = h , country = i ,state = j ,city = k , hobby = l , languages = m , 
        #     annual_income = n , about = o , status = p
        # )
        person.save()
        return HttpResponse("<script>window.alert('Congrats...! your Profile has been Updated');window.location.href=('/user/');</script>")
    else:
        return render(request, 'Profile.html',{'Data':person})