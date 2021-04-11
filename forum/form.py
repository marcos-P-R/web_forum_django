from django import forms
from .models import Post

class Insere_topico_form(forms.Form):
    class Meta:
        model = Post

        fields = [
            'title',
            'body_text',
            'name_author'
        ]