from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    date_create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length = 100)
    detail = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now=True,auto_now_add=False)
    due_date = models.DateField(auto_now=False)
    category = models.ManyToManyField(Category, blank=True)
    task = models.ManyToManyField(Task, blank=True)
    user  = models.ManyToManyField(User, blank=True) 
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


    
    
    
    
    