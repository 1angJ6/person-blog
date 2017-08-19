from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=20)
    last_update_date = models.DateField
    content = models.TextField
