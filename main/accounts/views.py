from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import random
from .models import Verify
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, logout, login


# Create your views here.


def user_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conform_password = request.POST.get('conform_password')
        if password == conform_password:
            if User.objects.filter(username=username).exists():
                return redirect('user_registration')
            elif User.objects.filter(email=email).exists():
                return redirect('user_registration')
            else:
                user = User.objects.create(username=username, email=email, password=password)
                user.set_password(password)
                user.save()

                verification_code = random.randint(0000, 9999)
                prof = Verify.objects.create(user=user, verification_code=verification_code)
                prof.save()

                Subject = 'Accounts Verification'
                Body = f'Your Verification code is : http://127.0.0.1:8000/accounts/verification/{verification_code}/'
                recipient_list = [email]
                Email_from = settings.EMAIL_HOST_USER
                send_mail(Subject, Body, Email_from, recipient_list)
                return redirect('user_registration')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def verification(request, verification_code):
    Verified = Verify.objects.get(verification_code=verification_code)
    Verified.is_verified = True
    Verified.save()
    return redirect('user_registration')


def user_logout(request):
    logout(request)
    return redirect('user_registration')


def dashboard(request):
    user = request.user
    uname = User.objects.get(username=user.username)
    if request.method =='POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = request.POST.get('password')
        password = request.POST.get('password')
        npassword = request.POST.get('npassword')
        cpassword = request.POST.get('cpassword')


    return render(request, 'dashboard.html',
                  {
                      'user': user
                  })
