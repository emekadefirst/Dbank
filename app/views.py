from decimal import Decimal
from datetime import datetime
from django.shortcuts import render
from django.db import transaction
from .models import CustomUser  # Import your custom user model
from .forms import LoginForm  # Assuming you have defined a LoginForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .forms import LoginForm, SubtractBalanceForm



def landing(request):
    return render(request, 'landing.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = CustomUser.objects.create_user(
                username, email, password1)  # Use CustomUser here
            user.save()
            auth.login(request, user)
            return redirect('main')
        else:
            error_message = 'Error creating account'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')



def logout(request):
    auth.logout(request)
    return redirect('home')



@login_required
def main(request):
    user = request.user
    balance = user.balance

    if request.method == 'POST':
        amount = Decimal(request.POST['amount'])  # Convert amount to Decimal
        if balance >= amount:  # Use 'greater than or equal to'
            nbal = balance - amount
            user.balance = nbal  # Update the user's balance attribute
            user.save()  # Save the user instance
            return redirect('main')
    else:
        form = SubtractBalanceForm()

    return render(request, 'index.html', {'user': user, 'balance': balance, 'form': form})
