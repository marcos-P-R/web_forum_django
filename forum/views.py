from django.shortcuts import render

from django.http import HttpResponse

from django.views import generic

from .models import Post

from .form import Insere_topico_form

# Create your views here.
class List(generic.ListView):
    model = Post
    template_name = "forum/post_list.html"


class Detail(generic.DetailView):
    model = Post
    template_name = "forum/detail.html"

class Create(generic.CreateView):
    model = Post
    template_name = "forum/new_thread.html"
    form_class = Insere_topico_form
    #success_url = reverse_lazy("forum:list")
