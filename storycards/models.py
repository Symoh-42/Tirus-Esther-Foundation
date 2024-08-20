from django.db import models
from django_resized import ResizedImageField
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

# Create your models here.
class StoryCard(BaseModel):
    image      = ResizedImageField(quality=90, upload_to="StoryCard/", default= "default.jpg")
    name        = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active      = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "StoryCards"
        ordering = ["-updated_at"]