from django.views.generic import ListView, DeleteView, DetailView

from .models import Post

from .form import Insere_topico_form

from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect

# Create your views here.
class List_thread(ListView):
    model = Post
    template_name = "forum/post_list.html"


class Detail_thread(DetailView):
    model = Post
    template_name = "forum/detail.html"

def delete_thread(request, id):
    thread = Post.objects.get(id=id)
    thread.delete()
    return redirect('forum:thread-list')

def new_thread(request):
    if request.method == "POST":
        form = Insere_topico_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('forum:detail', pk=post.pk)
    else:
        form = Insere_topico_form()
    return render(request, 'forum/new_thread.html', {'form': form})
    #success_url = reverse_lazy("forum:list")
