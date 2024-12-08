from django.shortcuts import render
from .models import myBlogContent
from django.shortcuts import get_object_or_404
# Create your views here.


def main_page(request):
    content = myBlogContent.objects.all()
    return render(request,'mainpage.html',{'posts':content})

def blog_page(request, post_id):
    post = get_object_or_404(myBlogContent, blogID=post_id)
    return render(request, 'show_post.html', {'post': post})

