from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from accounts.models import Profile
from django.db.utils import IntegrityError

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home_product')
        else:
            return render(request,'accounts/login.html', {'error':'Usuario o contraseña incorrecta'})
    return render(request,'accounts/login.html')

def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password_confirmation != password:
            return render(request, 'accounts/signup.html', {'error':'Las contraseñas no coinciden'})
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error':'Username is already in user'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        profile = Profile(user=user)
        profile.save()
        return redirect('login')

    return render(request,'accounts/signup.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
