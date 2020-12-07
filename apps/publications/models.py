from django.db import models
from apps.tags.models import Tag
from apps.comments.models import Comment


# Create your models here.
class Publications(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=30)
    date = models.DateField()
    content = models.TextField()
    likes = models.IntegerField()

    tags = models.ManyToManyField(Tag, related_name='publications')
    comments = models.ManyToManyField(Comment, related_name='publications')

    def __str__(self):
        return self.title
