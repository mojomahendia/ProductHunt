from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method=='POST':
    # User wants and new account now.
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': "Username has already taken."})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password2'])
                auth.login(request, user)
                return redirect('home')
            else: return render(request, 'signup.html', {'error': "Password didn't match."})
    else: #user wants to login
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': "Username or Password is incorrect."})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        return redirect('home')
