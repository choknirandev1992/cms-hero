from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import logout


# Create your views here.
def login(request):
 current_user = request.user
 if(current_user.id):
    return redirect('/')
 return render(request, 'account/login.html')

def checklogin(request):
    email = request.POST['email']
    password = request.POST['pass']
    username = User.objects.get(email=email.lower()).username
    user = auth.authenticate(request, username=username, password=password)

    if user is not None:
        auth.login(request, user)
        status = "success"

    else:
        status = "fail" 
    
    data = {
      'status': status
    }

    return JsonResponse(data)

def checkemail(request):
   email = request.POST['email']
   response = User.objects.filter(email=email).exists()
   data = {
      'status': response,
   }

   return JsonResponse(data)
   
def sitelogout(request):
    logout(request)
    return redirect('login')

     

 