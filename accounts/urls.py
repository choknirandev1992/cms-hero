from django.urls import path
from . import views
urlpatterns = [
  path('login',views.login, name="login"),  
  path('logout',views.sitelogout,name='logout'),
  path('checklogin', views.checklogin,name='checklogin'),
  path('checkemail',views.checkemail,name='checkemail'),
  path('checkusername',views.checkusername, name='checkusername'),
  path('edit-profile/<int:id>',views.editProfile,name='editprofile'),
  path('profile',views.profile,name='profile'),
  path('users',views.users,name='users'),
  path('add-new-user',views.addNewUser,name='addnewuser'),
  path('delete-user',views.deleteprofile,name='delete-user'),
]