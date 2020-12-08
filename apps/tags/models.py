from django.db import models


class Tag(models.Model):
    name = models.CharField('TagName', max_length=80)

    def __str__(self):
        return self.name
