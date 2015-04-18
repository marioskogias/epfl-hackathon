from django.db import models

class Article(models.Model):
    link = models.CharField(max_length=200)
    keywords = models.TextField()

class Relationship(models.Model):
    id1 = models.IntegerField(default=0)
    id2 = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

