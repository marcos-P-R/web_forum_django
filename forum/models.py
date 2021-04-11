from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    body_text = models.TextField()
    name_author = models.CharField(max_length=100)
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-creation",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return "/forum/%i/" % self.id
    
    