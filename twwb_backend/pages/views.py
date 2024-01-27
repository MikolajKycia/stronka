from django.shortcuts import render, redirect
from django.http import HttpResponse
from comments.models import Comment
from comments.forms import CommentForm


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

def new_comment_view(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect ('../gallery/')
    context = {
        'form': form,
    }

    return render(request, 'new_comment.html', context)
