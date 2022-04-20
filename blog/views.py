from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/blogs.html', {'blogs':blogs})

def blogarticle(request, blog_id):
    blogarticle = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blogarticle.html', {'blog':blogarticle})