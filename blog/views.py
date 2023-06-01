from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User

from blog.models import User, Post, Comment


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(status=1).order_by('-published_at')
    return render(request, 'post-list.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post-detail.html', {'post': post, 'comments': comments})
