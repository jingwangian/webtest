from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
from .models import Post

@require_http_methods(["GET", "POST"])
def blog_list(request):
    object_list = Post.objects.all()
    return render(request,'blog/blog_list.html',{'objects': object_list})
#     return HttpResponse('<p>This is blog list</p>')

def blog_detail(request,pk):
    object = Post.objects.get(pk=pk)
    return render(request, 'blog/blog_detail.html', {'object':object})