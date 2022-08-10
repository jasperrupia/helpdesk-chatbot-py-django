from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    if request.user.is_authenticated:
        return redirect('adminPanel:dashboard')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminPanel:dashboard')
        else:
            messages.success(request, ('Username or Password incorrect')) 
            return redirect('signin')
    else:
        return render(request, 'advanced/page_login.html')

def user_logout(request):
    logout(request)
    return redirect('signin')


