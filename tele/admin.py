from django.contrib import admin
from diskvem.diskvem.models import Empresa, Bairro, Cidade, Estado, Pais, Contato, Categoria, Telefone, Pagamento

class EmpresaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Pais)
admin.site.register(Contato)
admin.site.register(Categoria)
admin.site.register(Telefone)
admin.site.register(Pagamento)
