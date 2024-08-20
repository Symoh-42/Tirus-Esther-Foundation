from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.static import serve

from .forms import UserPasswordResetForm

from core import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    
    path("", views.home, name="home"),
    path("about/", include("about.urls")),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('allauth.urls')),
    path("blog/", include("blog.urls")),
    path("contact/", include("contact.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("programs/", include("programs.urls")),
    path("projects/", include("projects.urls")),
    path("storycards/", include("storycards.urls")),

    # FORGET PASSWORD
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/reset_password.html",
            form_class=UserPasswordResetForm,
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/reset_password_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/reset.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/reset_password_complete.html"
        ),
        name="password_reset_complete",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]


