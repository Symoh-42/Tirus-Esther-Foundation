from django.shortcuts import render
from projects.models import *

def projectsPage(request):
    projects = Project.objects.all()
    context = {
        "projects":projects
    }

    return render(request, "projects_pages/projects.html", context)

def singleProjectPage(request, slug):
    project = Project.objects.get(slug=slug)
    other_images = OtherProjectImages.objects.filter(project=project).all()

    context = {
        "project":project,
        "other_images":other_images
    }

    return render(request, "projects_pages/single_projects.html", context)
