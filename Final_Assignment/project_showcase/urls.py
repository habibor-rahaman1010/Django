from django.urls import path
from . import views 


urlpatterns = [
    path('all_project/', views.sgowAllProjects, name = 'All_Project'),    
]