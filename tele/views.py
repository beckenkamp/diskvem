from django.http import HttpResponse
from django.template.response import TemplateResponse
from tele.models import Empresa, Telefone
from tele.forms import SearchForm

def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            teste = form.cleaned_data['search_term']
    return TemplateResponse(request, 'tele/home.html', {'empresas': Empresa.objects.all(), 'teste': teste})
