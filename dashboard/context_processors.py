from contact.models import Contact
from programs.models import Program
from projects.models import Project
from .models import *

def unread_inquires(request):
    count_inquires = Contact.objects.filter(view=False).count()
    context = {
        "count_inquires":count_inquires
    }
    return context

def allPrograms(request):
    programs = Program.objects.filter(active=True).all()
    count_programs = programs.count()
    context = {
        "count_programs":count_programs,
        "programs":programs
    }
    return context

def allProjects(request):
    count_projects = Project.objects.filter(active=True).all().count()
    context = {
        "count_projects":count_projects
    }
    return context
