from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    title = models.CharField(
        max_length=2048,
        verbose_name="Post Title"
    )
    content = models.TextField(
        verbose_name="Content"
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Is Published?"
    )
    published_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Date Published"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']