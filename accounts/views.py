from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def login(request):
 return render(request, 'account/login.html')

    

