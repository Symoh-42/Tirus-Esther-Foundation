from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboardPage, name="dashboard"),

    path("team", views.teamPage, name="team"),
    path("add-team", views.addTeamPage, name="add_team"),
    path("edit-team/<str:id>", views.editTeamPage, name="edit_team"),
    path("activate-team/<str:id>", views.activateTeamPage, name="activate_team"),
    path("deactivate-team/<str:id>", views.deactivateTeamPage, name="deactivate_team"),

    path("testimonials", views.testimonialsPage, name="testimonials"),
    path("add-testimonials", views.addTestimonialsPage, name="add_testimonials"),
    path("edit-testimonials/<str:id>", views.editTestimonialsPage, name="edit_testimonials"),

    path("stories", views.storiesPage, name="stories"),
    path("add_story", views.addstoryPage, name="add_story"),
    path("edit_story/<str:id>", views.editstoryPage, name="edit_story"),
    path("activate_story/<str:id>", views.activatestoryPage, name="activate_story"),
    path("deactivate_story/<str:id>", views.deactivatestoryPage, name="deactivate_story"),

    path("inquiries", views.inquiriesPage, name="inquiries"),
    path("view_inquiry/<str:id>", views.viewInquiryPage, name="inquiry"),

    path("sponsors", views.sponsorsPage, name="sponsors"),
    path("add_sponsor", views.addSponsorPage, name="add_sponsor"),
    path("edit_sponsor/<str:id>", views.editSponsorPage, name="edit_sponsor"),
    path("activate_sponsor/<str:id>", views.activateSponsorPage, name="activate_sponsor"),
    path("deactivate_sponsor/<str:id>", views.deactivateSponsorPage, name="deactivate_sponsor"),

    path("programs", views.programsPage, name="view_programs"),
    path("add_program", views.addProgramPage, name="add_program"),
    path("edit_program/<str:id>", views.editProgramPage, name="edit_program"),
    path("active_program/<slug:slug>", views.activeProgramPage, name="active_program"),
    path("deactive_program/<slug:slug>", views.deactiveProgramPage, name="deactive_program"),
    
    path("projects", views.projectsPage, name="view_projects"),
    path("add_project", views.addProjectPage, name="add_project"),
    path("edit_project/<slug:slug>", views.editProjectPage, name="edit_project"),

    path("blogs", views.blogsPage, name="view_blogs"),
    path("add_blog", views.addBlogPage, name="add_blog"),
    path("edit_blog/<slug:slug>", views.editBlogPage, name="edit_blog"),

    path("settings", views.settingsPage, name="settings"),
    path("edit-settings-no-<str:pk>", views.editSettingsPage, name="edit_settings"),
]