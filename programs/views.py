from django.shortcuts import render
from programs.models import *
from contact.forms import *

def programsPage(request):
    programs = Program.objects.filter(active=True).all()
    context = {
        "programs":programs
    }

    return render(request, "programs_pages/programs.html", context)

def singleProgramsPage(request, slug):
    programs = Program.objects.filter(active=True).all()
    program = Program.objects.get(slug=slug)
    other_images = OtherProgramImages.objects.all()
    form = ContactForm
    context = {
        "programs":programs,
        "program":program,
        "other_images":other_images,
        "form":form
    }

    return render(request, "programs_pages/single_programs.html", context)