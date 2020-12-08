from django.db import models

from ..tags.models import Tag
from ..comments.models import Comment

class Publication(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    date = models.DateField()
    content = models.TextField()
    likes = models.IntegerField()

    tags = models.ManyToManyField(Tag, related_name='publications')
    comments = models.ManyToManyField(Comment, related_name='publications')

    def __str__(self):
        return self.title
