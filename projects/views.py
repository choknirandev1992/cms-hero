from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def project(request):
    return render(request, 'backend/project/index.html')

def projectDetail(request):
    return render(request,'backend/project/project-detail.html')

def addProject(request):
    return render(request,'backend/project/add-project.html')

def editProject(request):
    return render(request, 'backend/project/edit-project.html', {})
    
def deleteProject(request,id):
   data = {
        'status': '200',
   }

   return JsonResponse(data)