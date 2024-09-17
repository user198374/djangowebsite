from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title