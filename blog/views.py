"""
Blog app views.

Handles the blog listing page (with search and category filtering)
and individual blog post detail pages.
"""

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import BlogPost, BlogCategory


def blog_list_view(request):
    """Render the blog listing page with search and category filters."""
    posts = BlogPost.objects.filter(is_published=True)

    query = request.GET.get('q', '').strip()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(content__icontains=query)
        )

    category_slug = request.GET.get('category', '')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    context = {
        'posts': posts,
        'categories': BlogCategory.objects.all(),
        'query': query,
        'selected_category': category_slug,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail_view(request, slug):
    """Render an individual blog post detail page."""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    context = {
        'post': post,
        'recent_posts': BlogPost.objects.filter(is_published=True).exclude(slug=slug)[:3],
    }
    return render(request, 'blog/blog_detail.html', context)