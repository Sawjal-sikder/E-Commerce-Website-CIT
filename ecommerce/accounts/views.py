from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import random
from .models import Verify

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conform_password = request.POST.get('conform_password')
        if password == conform_password:
            if User.objects.filter(username=username).exists():
                return redirect('user_login')
            elif User.objects.filter(email=email).exists():
                return redirect('user_login')
            else:
                user = User.objects.create(username=username,email=email,password=password)
                user.set_password(password)
                user.save()

                otp = random.randint(000000,999999)


                
    return render(request, 'login_register.html')