from django.contrib import admin

from .models import Post

# Register your models here.

@admin.register(Post)

class Post_admin(admin.ModelAdmin):
    list_display = ("title", "name_author", "creation")