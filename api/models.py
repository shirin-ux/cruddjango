from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    year = models.IntegerField()
