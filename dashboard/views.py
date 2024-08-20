from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from .forms import *
from .models import *

from contact.models import Contact

from programs.forms import programForm, programImagesForm
from programs.models import Program, OtherProgramImages

from projects.forms import projectForm, projectImagesForm
from projects.models import Project, OtherProjectImages

from blog.models import BlogPost
from blog.forms import blogForm

from storycards.models import *
from storycards.forms import *


def dashboardPage(request):
    if request.user.is_staff == True:
        total_inquiries = Contact.objects.all()
        inquiries = total_inquiries[:5]
        inquiries_count = total_inquiries.count()
        
        blogs = BlogPost.objects.all()[:5]

        total_members = Team.objects.all()
        members = total_members[:5]
        members_count=total_members.count()

        all_programs = Program.objects.all()
        programs = all_programs[:5]
        programs_count = all_programs.count()

        all_projects = Project.objects.all()
        projects = all_projects[:5]
        projects_count = all_projects.count()

        context = {
            "inquiries_count":inquiries_count,
            "inquiries":inquiries,
            "members":members,
            "blogs":blogs,
            "members_count":members_count,
            "projects":projects,
            "projects_count":projects_count,
            "programs":programs,
            "programs_count":programs_count
        }

        return render(request, "dashboard_pages/index.html", context)

def teamPage(request):
    if request.user.is_staff == True:
        members = Team.objects.all()
        page = request.GET.get("page")
        results = 15
        paginator = Paginator(members, results)

        try:
            members = paginator.page(page)

        except PageNotAnInteger:
            page = 1
            members = paginator.page(page)

        except EmptyPage:
            page = paginator.num_pages
            members = paginator.page(page)

        context = {
            "members":members,
        }
        return render (request, "dashboard_pages/team_listing.html", context)

def testimonialsPage(request):
    if request.user.is_staff == True:
        testimonials = Testimonial.objects.all()
        page = request.GET.get("page")
        results = 15
        paginator = Paginator(testimonials, results)

        try:
            testimonials = paginator.page(page)

        except PageNotAnInteger:
            page = 1
            testimonials = paginator.page(page)

        except EmptyPage:
            page = paginator.num_pages
            testimonials = paginator.page(page)

        context ={
            "testimonials":testimonials
        }

        return render (request, "dashboard_pages/testimonials_listing.html", context)

def addTestimonialsPage(request):
    if request.user.is_staff == True:
        form = TestimonialForm

        if request.method == "POST":
            form = TestimonialForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Success! The testimony has been saved.")
                form = TestimonialForm
                return redirect('testimonials')
            else:
                messages.error(request, "Failed! The testimony was not saved.")
                form = TestimonialForm

        context ={
            "form":form
        }

        return render (request, "dashboard_pages/add_testimonials_listing.html", context)

def editTestimonialsPage(request, id):
    if request.user.is_staff == True:
        testimony = Testimonial.objects.get(id=id)
        form = TestimonialForm(instance=testimony)

        if request.method == "POST":
            form = TestimonialForm(request.POST, instance=testimony)

            if form.is_valid():
                form.save()
                messages.success(request, "Success! The testimony has been editted.")
                redirect('testimonials')
                form = TestimonialForm
                return redirect('testimonials')
            else:
                messages.error(request, "Failed! The testimony was not editted.")
                form = TestimonialForm

        context ={
            "form":form,
            "testimony":testimony
        }

        return render (request, "dashboard_pages/edit_testimonials.html", context)

def inquiriesPage(request):
    if request.user.is_staff == True:
        inquiries = Contact.objects.all()
        page = request.GET.get("page")
        results = 15
        paginator = Paginator(inquiries, results)

        try:
            inquiries = paginator.page(page)

        except PageNotAnInteger:
            page = 1
            inquiries = paginator.page(page)

        except EmptyPage:
            page = paginator.num_pages
            inquiries = paginator.page(page)

        context = {
            "inquiries":inquiries,
        }

        return render (request, "dashboard_pages/inquiries_listing.html", context)

def viewInquiryPage(request, id):
    if request.user.is_staff == True:
        inquiry = Contact.objects.get(id=id)

        if inquiry.view == False:
            inquiry.view = True
            inquiry.save()
            
        context = {
            "inquiry":inquiry
        }
        
        return render (request, "dashboard_pages/view_inquiry.html", context)


def addTeamPage(request):
    if request.user.is_staff == True:
        form = TeamForm

        if request.method == "POST":
            form = TeamForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                messages.success(request, "Success! Member has been saved.")
                form = TeamForm
                return redirect("team")

            else:
                messages.error(request, "Failed! Member was not saved.")
                form = TeamForm

        context = {
            "form":form
        }
        return render (request, "dashboard_pages/add_team.html", context)


def editTeamPage(request, id):
    if request.user.is_staff == True:
        team = Team.objects.get(id=id)
        form = TeamForm(instance=team)

        if request.method == "POST":
            form = TeamForm(request.POST, request.FILES, instance=team)

            if form.is_valid():
                form.save()
                messages.success(request, "Success! Member has been saved.")
                form = TeamForm
                return redirect("team")
            else:
                messages.error(request, "Failed! Member was not saved.")
                form = TeamForm

        context = {
            "form":form,
            "team":team
        }
        return render (request, "dashboard_pages/edit_team.html", context)
    
def activateTeamPage(request, id):
    if request.user.is_staff == True:
        team = Team.objects.get(id=id)

        if team.active == False:
            team.active = True
            team.save()

        return redirect("team")
    
def deactivateTeamPage(request, id):
    if request.user.is_staff == True:
        team = Team.objects.get(id=id)

        if team.active == True:
            team.active = False
            team.save()

        return redirect("team")


def sponsorsPage(request):
    if request.user.is_staff == True:
        sponsors = Sponsor.objects.all()
        page = request.GET.get("page")
        results = 15
        paginator = Paginator(sponsors, results)

        try:
            sponsors = paginator.page(page)

        except PageNotAnInteger:
            page = 1
            sponsors = paginator.page(page)

        except EmptyPage:
            page = paginator.num_pages
            sponsors = paginator.page(page)

        context = {
            "sponsors":sponsors,
        }

        return render (request, "dashboard_pages/sponsors_listing.html", context)

def addSponsorPage(request):
    if request.user.is_staff == True:
        form = SponsorForm

        if request.method == "POST":
            form = SponsorForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                messages.success(request, "Success! Sponsor has been saved.")
                form = SponsorForm
                return redirect("sponsors")

            else:
                messages.error(request, "Failed! Sponsor was not saved.")
                form = SponsorForm

        context = {
            "form":form
        }
        return render (request, "dashboard_pages/add_sponsor.html", context)

def editSponsorPage(request, id):
    if request.user.is_staff == True:
        sponsor = Sponsor.objects.get(id=id)
        form = SponsorForm(instance=sponsor)

        if request.method == "POST":
            form = SponsorForm(request.POST, request.FILES, instance=sponsor)

            if form.is_valid():
                form.save()
                messages.success(request, "Success! Sponsor has been saved.")
                form = SponsorForm
                return redirect("sponsors")

            else:
                messages.error(request, "Failed! Sponsor was not saved.")
                form = SponsorForm

        context = {
            "form":form,
            "sponsor":sponsor
        }
        return render (request, "dashboard_pages/edit_sponsor.html", context)

def activateSponsorPage(request, id):
    if request.user.is_staff == True:
        sponsor = Sponsor.objects.get(id=id)

        if sponsor.active == False:
            sponsor.active = True
            sponsor.save()

        return redirect("sponsors")
    
def deactivateSponsorPage(request, id):
    if request.user.is_staff == True:
        sponsor = Sponsor.objects.get(id=id)

        if sponsor.active == True:
            sponsor.active = False
            sponsor.save()

        return redirect("sponsors")

def programsPage(request):
    if request.user.is_staff == True:
        programs = Program.objects.all()
        page = request.GET.get("page")
        results = 15
        paginator = Paginator(programs, results)

        try:
            programs = paginator.page(page)

        except PageNotAnInteger:
            page = 1
            programs = paginator.page(page)

        except EmptyPage:
            page = paginator.num_pages
            programs = paginator.page(page)

        context = {
            "programs":programs,
        }

        return render (request, "dashboard_pages/programs_listing.html", context)

def addProgramPage(request):
    if request.user.is_staff == True:
        form = programForm
        other_images = programImagesForm

        if request.method == "POST":
            form = programForm(request.POST, request.FILES)
            imagesform = programImagesForm(request.POST, request.FILES)

            if form.is_valid():
                instance = form.save()

                if imagesform.is_valid():
                    images = request.FILES.getlist("other_program_images")

                    for image in images:
                        photo = OtherProgramImages.objects.create(
                            other_program_images=image, program=instance
                        )

                messages.success(request, "Program has been added successful.")

                return redirect("view_programs")

            else:
                messages.success(request, "An error occured during the process.")


        context = {
            "form":form,
            "other_images":other_images
        }
        return render (request, "dashboard_pages/add_program.html", context)


def editProgramPage(request, id):
    if request.user.is_staff == True:
        program = Program.objects.get(id=id)
        form = programForm(instance=program)
        other_images = programImagesForm(instance=program)

        if request.method == "POST":
            form = programForm(request.POST, request.FILES, instance=program)
            imagesform = programImagesForm(request.POST, request.FILES, instance=program)

            if form.is_valid():
                instance = form.save()

                if imagesform.is_valid():
                    images = request.FILES.getlist("other_program_images")

                    for image in images:
                        photo = OtherProgramImages.objects.create(
                            other_program_images=image, program=instance
                        )

                messages.success(request, "Program has been editted successful.")

                return redirect("view_programs")

            else:
                messages.success(request, "An error occured during the process.")


        context = {
            "form":form,
            "other_images":other_images,
            "program":program
        }
        return render (request, "dashboard_pages/edit_program.html", context)

def activeProgramPage(request, slug):
    if request.user.is_staff == True:
        program = Program.objects.get(slug=slug)

        if program.active == False:
            program.active = True
            program.save()

        return redirect("view_programs")
    
def deactiveProgramPage(request, slug):
    if request.user.is_staff == True:
        program = Program.objects.get(slug=slug)

        if program.active == True:
            program.active = False
            program.save()

        return redirect("view_programs")

def projectsPage(request):
    if request.user.is_staff == True:
        projects = Project.objects.all()
        page = request.GET.get("page")
        results = 15
        paginator = Paginator(projects, results)

        try:
            projects = paginator.page(page)

        except PageNotAnInteger:
            page = 1
            projects = paginator.page(page)

        except EmptyPage:
            page = paginator.num_pages
            projects = paginator.page(page)

        context = {
            "projects":projects,
        }

        return render (request, "dashboard_pages/projects_listing.html", context)

def addProjectPage(request):
    if request.user.is_staff == True:
        form = projectForm
        other_images = projectImagesForm

        if request.method == "POST":
            form = projectForm(request.POST, request.FILES)
            imagesform = projectImagesForm(request.POST, request.FILES)

            if form.is_valid():
                instance = form.save()

                if imagesform.is_valid():
                    images = request.FILES.getlist("other_project_images")

                    for image in images:
                        photo = OtherProjectImages.objects.create(
                            other_project_images=image, project=instance
                        )

                messages.success(request, "Program has been added successful.")

                return redirect("view_projects")

            else:
                messages.success(request, "An error occured during the process.")


        context = {
            "form":form,
            "other_images":other_images
        }
        return render (request, "dashboard_pages/add_project.html", context)

def editProjectPage(request, slug):
    if request.user.is_staff == True:
        project = Project.objects.get(slug=slug)
        form = projectForm(instance=project)
        other_images = projectImagesForm(instance=project)

        if request.method == "POST":
            form = projectForm(request.POST, request.FILES, instance=project)
            imagesform = projectImagesForm(request.POST, request.FILES, instance=project)

            if form.is_valid():
                instance = form.save()

                if imagesform.is_valid():
                    images = request.FILES.getlist("other_project_images")

                    for image in images:
                        photo = OtherProjectImages.objects.create(
                            other_project_images=image, project=instance
                        )

                messages.success(request, "Program has been added successful.")

                return redirect("view_projects")

            else:
                messages.success(request, "An error occured during the process.")


        context = {
            "form":form,
            "other_images":other_images,
            "project":project
        }
        return render (request, "dashboard_pages/edit_project.html", context)


def blogsPage(request):
    if request.user.is_staff == True:
        blogs = BlogPost.objects.all()
        page = request.GET.get("page")
        results = 15
        paginator = Paginator(blogs, results)

        try:
            blogs = paginator.page(page)

        except PageNotAnInteger:
            page = 1
            blogs = paginator.page(page)

        except EmptyPage:
            page = paginator.num_pages
            blogs = paginator.page(page)

        context = {
            "blogs":blogs,
        }

        return render (request, "dashboard_pages/blogs_listing.html", context)

def addBlogPage(request):
    if request.user.is_staff == True:
        form = blogForm
        if request.method == "POST":
            form = blogForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                messages.success(request, "Blog has been added successful.")

                return redirect("view_blogs")

            else:
                messages.success(request, "An error occured during the process.")

        context = {
            "form":form,
        }
        return render (request, "dashboard_pages/add_blog.html", context)

def editBlogPage(request, slug):
    if request.user.is_staff == True:
        blog = BlogPost.objects.get(slug=slug)
        form = blogForm(instance=blog)
        if request.method == "POST":
            form = blogForm(request.POST, request.FILES, instance=blog)

            if form.is_valid():
                form.save()

                messages.success(request, "Blog has been editted successful.")

                return redirect("view_blogs")

            else:
                messages.success(request, "An error occured during the process.")

        context = {
            "form":form,
            "blog":blog
        }
        return render (request, "dashboard_pages/edit_blog.html", context)


def settingsPage(request):
    if request.user.is_staff == True:
        setting = Settings.objects.all()

        context = {
            "setting":setting
        }
    
        return render (request, "dashboard_pages/settings.html", context)

def editSettingsPage (request, pk):
    if request.user.is_staff == True:
        setting = Settings.objects.get(id=pk)
        form = settingsForm(instance=setting)

        if request.method == "POST":
            form = settingsForm(request.POST, request.FILES, instance=setting)

            if form.is_valid():
                form.save()

                messages.success(request, "Thank you! Updates have been successful.")

            else:
                messages.error(request, "Failed! Updates have not been  successful.")

        context = {
            "setting":setting,
            "form" :form
        }
        return render(request, "dashboard_pages/edit_settings.html", context)
    

def storiesPage (request):
    stories = StoryCard.objects.all()
    context ={
        "stories":stories
    }

    return render(request, 'dashboard_pages/stories_listing.html', context)

def addstoryPage (request):
    if request.user.is_staff == True:
        form = StoryCardForm
        if request.method == "POST":
            form = StoryCardForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                messages.success(request, "Story card has been added successful.")

                return redirect("stories")

            else:
                messages.success(request, "An error occured during the process.")

    context ={
        "form":form
    }

    return render(request, 'dashboard_pages/add_story.html', context)

def editstoryPage (request, id):
    if request.user.is_staff == True:
        story = StoryCard.objects.get(id=id)
        form = StoryCardForm(instance=story)
        if request.method == "POST":
            form = StoryCardForm(request.POST, request.FILES, instance=story)

            if form.is_valid():
                form.save()

                messages.success(request, "Story card has been editted successful.")

                return redirect("stories")

            else:
                messages.success(request, "An error occured during the process.")

        context ={
            "form":form,
            "story":story
        }
    return render(request, 'dashboard_pages/edit_story.html', context)

def activatestoryPage (request, id):
    if request.user.is_staff == True:
        story = StoryCard.objects.get(id=id)

        if story.active == False:
            story.active = True
            story.save()

        return redirect("stories")

def deactivatestoryPage (request, id):
    if request.user.is_staff == True:
        story = StoryCard.objects.get(id=id)

        if story.active == True:
            story.active = False
            story.save()

        return redirect("stories")