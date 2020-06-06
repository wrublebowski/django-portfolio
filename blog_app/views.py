from django.shortcuts import render, get_object_or_404
from blog_app.models import BlogProject

# Create your views here.
def all_blogs(request):
    # .order_by('-date') to sort blogs descending
    # .all() to show all
    # to show
    blog_projects = BlogProject.objects.order_by("-date")
    return render(request, 'blog_app/all_blogs.html', {'blog_projects':blog_projects})

def detail(request, blog_id):
    blog = get_object_or_404(BlogProject, pk=blog_id)
    return render(request, 'blog_app/detail.html', {'blog':blog})
