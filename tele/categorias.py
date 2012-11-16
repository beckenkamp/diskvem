from tele.models import Empresa, Telefone, Categoria
from django.db.models import Q
import operator

class Categorias:
    
    def list(self):
        lista = []
        
        for categoria in Categoria.objects.all():
            if not categoria.parent:
                lista.append([categoria, self.get_sub(categoria)])
        
        return lista
    
    def get_sub(self, cat):
        lista = []
        
        for categoria in Categoria.objects.filter(parent=cat):
            lista.append([categoria, self.get_sub(categoria)])
            
        return lista
    
    def get_empresas_by_categoria(self, cat):
        categorias = Categoria.objects.filter(parent=cat)
        qtd = categorias.count()
        
        if qtd > 0:
            filters = reduce(operator.or_, (Q(categoria=cat) | Q(categoria=cat) for cat in categorias))
        else:
            filters = Q(categoria=cat)
            
        empresas = Empresa.objects.filter(filters)
            
        return empresas
        
