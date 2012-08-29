from tele.models import Categoria

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
