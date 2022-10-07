from django.db import models


# Create your models here.
class News(models.Model):
    topic = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    create_time = models.DateTimeField("create time")
    last_edit_time = models.DateTimeField("last edit time")
