from django.shortcuts import render , HttpResponse, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from .models import User
# In another file
from myapp.models import User

from django.contrib import auth
from django.contrib.auth.hashers import check_password

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Use your custom user model if you have one
from django.http import HttpResponse

def home_page(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(username, email, password1, password2)

        # Check if passwords match
        if password1 != password2:
            return HttpResponse('Passwords do not match.')

        # Check if the username or email is already taken
        if User.objects.filter(username=username).exists():
            return HttpResponse('Username is already taken.')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Email is already taken.')

        # Create a new User instance
        new_user = User(username=username, email=email, password=password1)

        # Set the password using set_password method for proper hashing
        new_user.set_password(password1)

        # Save the instance to the database
        new_user.save()

        # Redirect to a success page or wherever you want to go after successful signup
        return redirect('login/')

    return render(request, 'myapp/home_page.html')

def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password1 = request.POST.get('password1')
        print(name, password1)
        
        user = auth.authenticate(request, username=name, password=password1)
        print("user", user)


        if user is not None and check_password(password1, user.password):
        # Authentication successful
            print(f"Authentication successful for username: {name}")
            return redirect('index_page')
        # ya page var redirect zal pahije
            # return HttpResponse("login successfully")
        else:
        # Authentication failed
            print(f"Authentication failed for username: {name}")
            return redirect('/')

       
    else:
        return render(request, 'myapp/login_page.html')
                
    

def signup_page(request):
    return render(request, 'myapp/signup_page')



def index_page(request):
    return render(request, 'myapp/index_page.html')

















