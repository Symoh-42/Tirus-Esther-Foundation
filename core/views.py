from django.shortcuts import render
from programs.models import Program
from projects.models import Project
from dashboard.models import *
from blog.models import *

def home (request):
    programs = Program.objects.filter(active=True).all()
    projects = Project.objects.filter(active=True).all()[:4]
    testimonials = Testimonial.objects.filter(active=True).all()[:4]
    sponsors_team = Sponsor.objects.filter(active=True).all()
    team = Team.objects.filter(active=True).all()
    blogs = BlogPost.objects.filter(published=True).all()

    context = {
        "programs":programs,
        "projects":projects,
        "testimonials":testimonials,
        "sponsors_team":sponsors_team,
        "team":team,
        "blogs":blogs
    }

    return render (request, "index.html", context)