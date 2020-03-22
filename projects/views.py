from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Project,Category,Task
from django.contrib.auth.models import User

# Create your views here.
def project(request):
    project = Project.objects.all().order_by('-date_create')
    paginator = Paginator(project, 20)
    page = request.GET.get('page')
    project = paginator.get_page(page)

    context = {
      "project" : project
    }

    return render(request, 'backend/project/index.html',context)

def projectDetail(request):
    return render(request,'backend/project/project-detail.html')

def addProject(request):
    category = Category.objects.all()
    user = User.objects.all()
    context = {
        "category" : category,
        "user" : user
    }
    return render(request,'backend/project/add-project.html', context)

def saveNewProject(request):
    if request.method == 'POST':
      project_name = request.POST['project_name']
      detail = request.POST.get('detail', '')
      due_date = request.POST['due_date']
      status = request.POST['status']
      category = request.POST.getlist('category')
      user_data = request.POST.getlist('user')
      project = Project(name=project_name, detail=detail, due_date=due_date, status=status)
      project.save()

      for cats in category:
        project.category.add(cats)

      for users in user_data:
        project.user.add(users)


      return redirect('project')

def projectCategory(request):
    return render(request,'backend/project/project-category.html')
    
def editProject(request):
    return render(request, 'backend/project/edit-project.html')
    
def deleteProject(request,id):
   data = {
        'status': '200',
   }

   return JsonResponse(data)