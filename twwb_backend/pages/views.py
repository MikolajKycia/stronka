from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def gallery_view(request, *args, **kwargs):
    return render(request, "gallery.html", {})
