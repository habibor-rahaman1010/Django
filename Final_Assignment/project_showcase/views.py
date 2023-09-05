from django.shortcuts import render

from .models import Project

# Create your views here.
def sgowAllProjects(request):
    project = Project.objects.all()
    return render(request, 'show_all_project.html', context={'project':project})