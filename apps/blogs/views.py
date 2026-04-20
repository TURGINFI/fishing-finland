from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BlogPostForm
from .models import BlogPost


def public_blog_list(request):
    posts = BlogPost.objects.filter(status=BlogPost.Status.APPROVED).order_by('-created_at')
    return render(request, 'blogs/public_list.html', {'posts': posts})


def public_blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, status=BlogPost.Status.APPROVED)
    return render(request, 'blogs/detail.html', {'post': post})


@login_required
def my_blog_list(request):
    posts = BlogPost.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blogs/my_list.html', {'posts': posts})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = BlogPost.Status.PENDING
            post.save()
            messages.success(request, 'Blog post submitted for review.')
            return redirect('my_blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blogs/form.html', {'form': form})
