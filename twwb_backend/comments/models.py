from django.db import models


# Create your models here.
class Comment(models.Model):
    author = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
