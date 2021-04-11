from django.shortcuts import render

from django.http import HttpResponse

from django.views import generic

from .models import Post

# Create your views here.
class List(generic.ListView):
    model = Post
    #template_name = "TEMPLATE_NAME"


class Detail(generic.DetailView):
    model = Post
    #template_name = "TEMPLATE_NAME"

