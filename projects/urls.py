from django.urls import path
from . import views

urlpatterns = [
  path('',views.project, name="project"),
  path('add-new',views.addProject, name="add_project"),
  path('save-project',views.saveNewProject, name="save_new_project"),
  path('detail',views.projectDetail, name="project_detail"),
  path('edit',views.editProject, name="edit_project"),
  path('category',views.projectCategory, name="project_category"),  
  path('delete/<int:id>',views.deleteProject,name='delete_project'),  
]