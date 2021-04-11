from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    body_text = models.TextField()
    name_author = models.ForeignKey(User, on_delete=models.CASCADE)