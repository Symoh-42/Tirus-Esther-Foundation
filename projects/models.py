from django.db import models
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify
from django.utils.text import slugify
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

class Project(BaseModel):
    title         = models.CharField(max_length=200, blank=True, null=True)
    description   = models.TextField(blank=True, null=True)
    main_image    = ResizedImageField(quality=90, upload_to="project/")
    completed     = models.BooleanField(default=False, blank=True, null=True)
    in_progress   = models.BooleanField(default=False, blank=True, null=True)
    youtube_link  = models.CharField(max_length=200, blank=True, null=True)
    active        = models.BooleanField(default=False, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    
    class Meta:
        verbose_name_plural = "Projects"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
class OtherProjectImages(BaseModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    
    other_project_images = ResizedImageField(quality=90, upload_to="project/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Other project images"

    def __str__(self):
        return self.project.title