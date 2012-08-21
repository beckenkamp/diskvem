from django.http import HttpResponse
from django.template.response import TemplateResponse
from tele.models import Empresa

def home(request):
    return TemplateResponse(request, 'tele/home.html', {'empresas': Empresa.objects.all()})
