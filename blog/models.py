from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
from django.utils.text import slugify
import uuid
from django.utils import timezone

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    class Meta:
        abstract = True


class BlogPost(BaseModel):
    author = models.CharField(max_length=200, null=True, blank=True, unique=True)
    title = models.CharField(max_length=200, null=True, blank=True, unique=True)
    blog_description = RichTextField()
    cover_image = models.ImageField(blank=True, upload_to="blogcover")
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    read_count = models.IntegerField(default=0, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    # publish_date = models.DateTimeField(null=True, blank=True, default=0)


    class Meta:
        verbose_name_plural = "Blog Posts"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comments(BaseModel):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    status = models.BooleanField(default=True)
    is_censored = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment by {self.name}"
