from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


# Create your views here.

# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            auth_login(request, user)
            messages.success(request, 'Login successful!')  # Optional: Add a success message
            return redirect('user_list')  # Redirect to the dashboard or home page after login
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'myapp/login.html')

def signup(request):
    if request.method == "POST":
        # Get data from the form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'myapp/signup.html')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken. Please choose another one.')
            return render(request, 'myapp/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use another email.')
            return render(request, 'myapp/signup.html')

        # Hash the password before saving
        hashed_password = make_password(password)

        # Create and save the new user
        user = User(username=username, email=email, password=hashed_password)
        user.save()

        # Add a success message
        messages.success(request, 'Registration successful! You can now log in.')

        # Redirect to the login page or home page after successful registration
        return redirect('login')  # Replace 'login' with the appropriate URL or view name for login

    return render(request, 'myapp/signup.html')

def predict(request):
    return render(request, 'myapp/StrokePrdedectionDashboard.html')

def user_list(request):
    # Fetch all users from the database
    users = User.objects.all()

    # Render the template with the users data
    return render(request, 'myapp/user_list.html', {'users': users})


