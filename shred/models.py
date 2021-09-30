from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Beach(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now=True)
    image = models.TextField(blank = True)
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.user