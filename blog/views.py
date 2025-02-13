from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from .models import Post

def post_list(request):
    posts = Post.published.all()

    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, id):

    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

    try: 
        post = Post.published.ged(id=id)

    except Post.DoesNotExist:
        raise Http404("No Post found")
    
    return render(
        request,
        'blog/post/detail.html',
        {'post':post}
    )