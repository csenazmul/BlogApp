from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Django 5 the database servers current date
# from django.db.models.functions import Now  
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    # author = models.ForeignKey(User, on_delete=models.CASCADE)  # Writer
    publish = models.DateTimeField(default=timezone.now)
    # publish = models.DateTimeField(db_default=Now()) # Django 5 the database servers current date
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    objects = models.Manager() # the default manager
    published = PublishedManager() # Our custom manager

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title