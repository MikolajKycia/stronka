from django.shortcuts import render
from django.http import HttpResponse
from comments.models import Comment


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def gallery_view(request, *args, **kwargs):
    context = {
        'comments': Comment.objects.all(),
    }
    return render(request, "gallery.html", context)

def about_view(request):
    return render(request, 'about.html')
