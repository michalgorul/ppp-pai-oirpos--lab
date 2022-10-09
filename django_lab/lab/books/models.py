from django.db import models


# Create your models here.


class Book(models.Model):
    topic = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    create_time = models.DateTimeField("create time")
    last_edit_time = models.DateTimeField("last edit time")
