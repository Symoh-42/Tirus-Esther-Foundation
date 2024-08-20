from django.shortcuts import render
from django.contrib import messages
from .forms import *


# Create your views here.
def contactPage(request):
    form = ContactForm

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your Message has been sent.")
            form = ContactForm

        else:
            messages.error(request, "Failed! Your message was not sent.")
            form = ContactForm

    context = {"form": form}

    return render(request, "contact_pages/contact.html", context)
