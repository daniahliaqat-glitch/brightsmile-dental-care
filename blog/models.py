"""
Blog app models.

Handles dental blog articles organized into categories such as
Dental Tips, Oral Hygiene, Kids Dental Care, Braces Guide, and
Teeth Whitening, with search support.
"""

from django.db import models
from django.conf import settings


class BlogCategory(models.Model):
    """A category used to organize blog posts."""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """A single blog article."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='blog_posts',
    )
    featured_image = models.ImageField(upload_to='blog/')
    excerpt = models.CharField(
        max_length=300,
        help_text="Short summary shown on the blog listing page."
    )
    content = models.TextField()

    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title