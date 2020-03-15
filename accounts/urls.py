from django.urls import path
from . import views
urlpatterns = [
  path('login',views.login, name="login"),  
  path('logout',views.sitelogout,name='logout'),
  path('checklogin', views.checklogin,name='checklogin'),
  path('checkemail',views.checkemail,name='checkemail'),
  
]