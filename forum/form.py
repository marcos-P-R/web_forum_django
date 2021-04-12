from django.forms import ModelForm
from .models import Post #Answer

class Insere_topico_form(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body_text', 'name_author',)

#class Insere_resposta(ModelForm):
#    class Meta:
#        model = Answer
#        fields = ('text_answer', 'name',)