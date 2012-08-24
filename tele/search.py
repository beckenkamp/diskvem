from tele.models import Empresa, Telefone, Tag, Bairro
from django.db.models import Q
import operator

class Search:
    #unsearchable_terms = {'na', 'no', 'em', 'do', 'de', 'da', 'a', 'o', 'e'}
    
    def do_search(self, search_term, search_bairro):
        split_terms = search_term.split(' ')
        qtd_tags = 0
        qtd_bairros = 0
        
        for term in split_terms:
            qtd_tags = Tag.objects.filter(nome__contains=term).count() + qtd_tags

        filters = reduce(operator.or_, (Q(nome__contains=term) | Q(tag__nome__contains=term) for term in split_terms))
        
        query_set = Empresa.objects.select_related().filter(filters, bairro=search_bairro, ativo=True).distinct()
        return query_set