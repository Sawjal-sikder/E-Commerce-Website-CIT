from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='user_login')
def dashboard(request):
    user = request.user
    return render(request,'dashboard.html',locals())