from django.shortcuts import render, get_object_or_404
from dashboard.models import *

def aboutPage(request):
    sponsors_team = Sponsor.objects.filter(active=True).all()
    team = Team.objects.filter(active=True).all()
    
    context = {
        "sponsors_team":sponsors_team,
        "team":team
    }

    return render(request, "about_pages/about.html", context)

def leadershipPage(request):
    team = Team.objects.filter(active=True).all()
    context = {
        "team":team
    }

    return render(request, "about_pages/leadership.html", context)

def partnershipPage(request):
    sponsors = Sponsor.objects.filter(active=True).all()
    context = {
        "sponsors":sponsors
    }

    return render(request, "about_pages/parternship.html", context)

def singleTeamPage(request, id):
    team = get_object_or_404(Team, id=id)
    context = {
        "team":team
    }

    return render(request, "about_pages/single_page.html", context)
