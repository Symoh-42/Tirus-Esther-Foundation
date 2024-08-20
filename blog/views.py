from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

def blogsPage(request):
    blogs = BlogPost.objects.all()
    comments = Comments.objects.all()
    context = {
        "blogs":blogs,
        "comments":comments
    }

    return render(request, "blogs_pages/blogs.html", context)


def singleBlogsPage(request, slug):
    blogs = BlogPost.objects.all()[:5]
    blog= get_object_or_404(BlogPost, slug=slug)

    comments = Comments.objects.filter(blog=blog)
    comment_form = CommentForm
    if request.method == 'POST':
          comment_form = CommentForm(request.POST)
          if comment_form.is_valid():
               user_comment = comment_form.save(commit = False)
               user_comment.blog = blog
               user_comment.save()
               messages.success(request, "Thank you! Your reply has been sent.")

               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    context = {
        "blog":blog,
        "comments":comments,
        "comment_form":comment_form,
        "blogs":blogs
    }

    return render(request, "blogs_pages/single_blog.html", context)
