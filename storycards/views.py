from django.shortcuts import render
from .models import StoryCard

# Create your views here.
def storyPage (request):
    stories = StoryCard.objects.filter(active=True).all()
    context = {
        "stories":stories
    }
    return render (request, "story/storycard.html", context)