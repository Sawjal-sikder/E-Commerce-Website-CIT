from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import Address
from django.contrib.auth.forms import PasswordChangeForm

@login_required(login_url='user_login')
def dashboard(request):
    user = request.user
    user_address = Address.objects.get(user=user)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        current_password = request.POST.get('current_password')
        npassword = request.POST.get('npassword')
        cpassword = request.POST.get('cpassword')

        if user.check_password(current_password):
            if npassword == cpassword:
                if User.objects.filter(email=email).exclude(pk=user.pk).exists():
                    messages.error(request, 'Email already in use.')
                else:
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email
                    user.set_password(npassword)
                    user.save()
                    print(user)
                    update_session_auth_hash(request, user)  # Important to keep the user logged in
                    messages.success(request, 'Profile updated successfully.')
                    return redirect('dashboard')
            else:
                messages.error(request, 'New passwords do not match.')
        else:
            messages.error(request, 'Current password is incorrect.')

    return render(request, 'dashboard.html', {'user': user, 'user_address': user_address})
