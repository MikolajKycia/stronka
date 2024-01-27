from django.shortcuts import render
from .models import Comment


# Create your views here.
def forum_view(request, *args, **kwargs):
    context = {
        'all_comments': Comment.objects.all(),
        }
    

    return render(request, 'forum.html', context)