from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date


class Genre(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Albums(models.Model):

    title = models.CharField(max_length=20)
    albumId = models.CharField(max_length=10)
    year = models.DateField()
    cover = models.ImageField(upload_to='albums/')
    genre = models.ManyToManyField('Genre', related_name='genres')

    def __str__(self):
        return self.title


class Artists(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    cover = models.ImageField(upload_to='artists/')
    bio = models.TextField()

    albums = models.ManyToManyField('Albums', related_name='record')    
    def __str__(self):
        return self.name

