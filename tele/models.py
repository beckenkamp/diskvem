from django.db import models

class Pais(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado)
    ddd = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome


class Bairro(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __unuicode__(self):
        return self.nome


class Categoria(models.Model):
    parent = models.ForeignKey('self')
    nome = models.CharField(max_length=100)
    slug = models.SlugField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome


class Pagamento(models.Model):
    nome = models.CharField(max_length=100)
    bandeira = models.CharField(max_length=100, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome


class Empresa(models.Model):
    cnpj = models.CharField(max_length=14, blank=True)
    nome = models.CharField(max_length=200)
    slug = models.SlugField()
    endereco = models.CharField(max_length=300, blank=True)
    bairro = models.ManyToManyField(Bairro)
    pagamento = models.ManyToManyField(Pagamento)
    categoria = models.ManyToManyField(Categoria)
    verificado = models.BooleanField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    empresa = models.ForeignKey(Empresa)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome


class Telefone(models.Model):
    number = models.IntegerField()
    empresa = models.ForeignKey(Empresa)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.number
