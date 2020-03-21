from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.db import models
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib import auth

# Create your views here.
def login(request):
    current_user = request.user
    if(current_user.id):
        return redirect('/')
    return render(request, 'account/login.html')

def editProfile(request,id):
    profile = get_object_or_404(Profile, pk=id)
    userid = profile.user.id
    user = get_object_or_404(User, pk=userid)
    if request.method == 'POST':
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      user_email = request.POST['user_email']
      user_phone = request.POST['user_phone']
      user_photo = request.FILES.get('user_photo', '')
      user_pass = request.POST.get('user_pass', '')
      
      #update user date
      user.first_name = first_name
      user.last_name = last_name
      user.email = user_email
      #update user pass
      if(user_pass):
         user.set_password(user_pass)
      user.save()

      #update user profile data
      profile.user_phone = user_phone
      #update user profile
      if(user_photo):
         profile.user_photo = user_photo
      profile.save()
    
    profile_after_update = get_object_or_404(Profile, pk=id)
    context = {
      "profile" : profile_after_update
    }

    return render(request,'backend/account/edit-profile.html',context)

def addNewUser(request):
   if request.method == 'POST':

      #get parameter 
      user_login = request.POST['user_login']
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      user_email = request.POST['user_email']
      user_phone = request.POST['user_phone']
      user_pass = request.POST['user_pass']
      user_photo = request.FILES['user_photo']
      
      #create user
      user = User.objects.create_user(user_login, user_email, user_pass )
      user.first_name = first_name
      user.last_name = last_name
      
      #save user
      user.save()

      #save user Profile
      profile = Profile(user=user, user_photo=user_photo, user_phone=user_phone)
      profile.save()
      return redirect('users')

   context = {}
   return render(request, 'backend/account/add-new-user.html',context)

def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user = current_user.id)
    profile_id = profile[0].id
    profile = get_object_or_404(Profile, pk=profile_id)
    user = get_object_or_404(User, pk=current_user.id)
    if request.method == 'POST':
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      user_email = request.POST['user_email']
      user_phone = request.POST['user_phone']
      user_photo = request.FILES.get('user_photo', '')
      user_pass = request.POST.get('user_pass', '')
      
      #update user date
      user.first_name = first_name
      user.last_name = last_name
      user.email = user_email
      #update user pass
      if(user_pass):
         user.set_password(user_pass)
      user.save()

      #update user profile data
      profile.user_phone = user_phone
      #update user profile
      if(user_photo):
         profile.user_photo = user_photo
      profile.save()
    
    profile_after_update = get_object_or_404(Profile, pk=profile_id)

    context = {
      "profile" : profile_after_update
    }

    return render(request,'backend/account/profile.html', context)

def users(request):
    if request.GET.get('s'):
      username =  request.GET.get('username')
      first_name =  request.GET.get('first_name')
      email =  request.GET.get('email')
      phone =  request.GET.get('phone')
      
      filters = Q()
      if first_name:
         filters &= models.Q(
            user__first_name__contains=first_name,
         )
      
      if username:
         filters &= models.Q(
            user__username__contains=username,
         )

      if email:
         filters &= models.Q(
            user__email__contains=email,
         )

      if phone:
         filters &= models.Q(
            user_phone__contains=phone,
         )

      profile = Profile.objects.filter(filters)
   
    else:
      profile = Profile.objects.all()

    paginator = Paginator(profile, 20)
    page = request.GET.get('page')
    profile = paginator.get_page(page)

    context = {
      "profile" : profile
    }

    return render(request,'backend/account/index.html',context)

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
   
def checkusername(request):
   username = request.POST['username']
   response = User.objects.filter(username=username).exists()
   data = {
      'status': response,
   }

   return JsonResponse(data)


def deleteprofile(request):
   profile_id = request.POST['user_id']
   profile = get_object_or_404(Profile, pk = profile_id)
   userid = profile.user_id
   profile.delete()
   
   user = User.objects.get(id=userid)
   user.delete()

   data = {
        'status': '200',
   }

   return JsonResponse(data)

def sitelogout(request):
    logout(request)
    return redirect('login')

     

 