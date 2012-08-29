from django.http import HttpResponse
from django.template.response import TemplateResponse
from tele.models import Empresa, Telefone
from tele.forms import SearchForm
import tele.search as search_class
import tele.categorias as categorias_class

def home(request):
    
    cat = categorias_class.Categorias()
    category_list = cat.list()
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            search_bairro = form.cleaned_data['search_bairro']
            search = search_class.Search()
            empresas = search.do_search(search_term, search_bairro)            
            return TemplateResponse(request, 'tele/home.html', {'form': form, 'categorias': category_list, 'empresas': empresas, 'search_term': search_term})
        else:
            return TemplateResponse(request, 'tele/home.html', {'form': form, 'categorias': category_list})
        
    else:
        form = SearchForm()
        return TemplateResponse(request, 'tele/home.html', {'form': form, 'categorias': category_list})
        
