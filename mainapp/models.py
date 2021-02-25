from django.db import models

# Create your models here.

# 1. Post

class Post(models.Model):

    post_id = models.PositiveIntegerField(unique=True, verbose_name='ID of Hacker News post')
    title = models.CharField(max_length=255, verbose_name='Title')
    url = models.URLField(verbose_name='Post URL')
    created = models.DateField(verbose_name='Date of created')

    def __str__(self):
        return f'{self.id}: Post #{self.post_id} - {self.title}'
