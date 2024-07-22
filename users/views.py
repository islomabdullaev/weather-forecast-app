from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pages:index')
    return render(request=request, template_name="registration/signin.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Already Created !")
        
        if not password == confirm_password:
            return HttpResponse("Password do not match !")
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('pages:index')

    return render(request=request, template_name="registration/signup.html")


def signout(request):
    logout(request)
    return redirect('users:login')