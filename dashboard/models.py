from django.db import models
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
import uuid

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    class Meta:
        abstract = True


class Testimonial(BaseModel):
    name      = models.CharField(max_length=200, blank=True, null=True)
    message   = models.TextField(blank=True, null=True)
    active    = models.BooleanField(default=False, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Testimonials"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name
    
class Team(BaseModel):
    name        = models.CharField(max_length=200, blank=True, null=True)
    position    = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image       = ResizedImageField(quality=90, upload_to="team/")
    active      = models.BooleanField(default=False, blank=True, null=True)

    
    class Meta:
        verbose_name_plural = "Teams"
        ordering = ["updated_at"]

    def __str__(self):
        return self.name
    
class Sponsor(BaseModel):
    image      = ResizedImageField(quality=90, upload_to="sponsor/", default= "default.jpg")
    name        = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active      = models.BooleanField(default=False, blank=True, null=True)
    link        = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sponsors"
        ordering = ["-updated_at"]


class Settings(BaseModel):
    phone = models.CharField(max_length=300, null=True, blank=True)
    phone2 = models.CharField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    google_map = models.CharField(max_length=500, null=True, blank=True)
    main_logo = ResizedImageField(quality=90, upload_to="logo/")
    mail_account = models.CharField(max_length=300, null=True, blank=True)
    
    about = models.TextField(null=True, blank=True)
    vision = models.TextField(null=True, blank=True)
    mission = models.TextField(null=True, blank=True)
    core = models.TextField(null=True, blank=True)
    objectives = RichTextField()
    
    facebook = models.CharField(max_length=300, null=True, blank=True)
    tiktok = models.CharField(max_length=300, null=True, blank=True)
    instagram = models.CharField(max_length=300, null=True, blank=True)
    twitter = models.CharField(max_length=300, null=True, blank=True)
    youtube = models.CharField(max_length=300, null=True, blank=True)
    pinterest = models.CharField(max_length=300, null=True, blank=True)
    

    class Meta:
        verbose_name_plural = "Settings"

    def __str__(self):
        return self.phone

