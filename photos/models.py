from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=150)
    image = models.FilePathField(path='../PantanaBobs/static/images')


