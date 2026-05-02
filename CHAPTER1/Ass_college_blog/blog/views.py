from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Post
def blog_list(request):
    Blog = Post.objects.all()    
    return render(request, 'blog/blog.html', {'blog': Blog})


def title_detail(request,id):
    # try:
    #     post=Post.Published.get(id=id)

    # except Post.DoesNotExist:
    #     raise Http404("post not found")
    # # return(request,'blog/title.html',{'title':title})
    post= get_object_or_404(
        Post,id=id,status=Post.Status.PUBLISHED
    )
    return render(request,'blog/title.html',{'post':post})