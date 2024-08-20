from django.db import models
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


class Contact(BaseModel):
    name    = models.CharField(max_length=200, blank=True, null=True)
    email   = models.EmailField(blank=True, null=True)
    phone   = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    view    = models.BooleanField(default=False, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Inquiries"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name
