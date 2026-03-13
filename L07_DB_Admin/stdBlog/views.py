from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post
def blog_list(request):
    # Blog = Post.objects.all()
    # Blog= Post.objects.all().order_by('-publish')
    # Blog= Post.objects.filter(status='publish').order_by('publish')
    # Blog=Post.objects.filter(body='created').order_by('-publish')
    Blog= Post.objects.filter(status='PB')
    return render(request, 'stdBlog/blog.html', {'blog': Blog})