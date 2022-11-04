from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    name = models.CharField('名前', max_length=20)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)