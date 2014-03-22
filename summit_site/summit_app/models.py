from django.db import models
from djangotoolbox.fields import ListField


# Example models
class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    tags = ListField()
    comments = ListField()

class Article(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
