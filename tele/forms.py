from django import forms
from tele.models import Bairro

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=300)
    search_bairro = forms.ModelChoiceField(queryset=Bairro.objects.all(), empty_label="Escolha um bairro")
