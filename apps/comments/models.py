from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=30)
    date = models.DateField()
    email = models.EmailField(max_length=50)
    content = models.TextField()
    likes = models.IntegerField()

    def __str__(self):
        return self.author
