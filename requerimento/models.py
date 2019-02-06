from django.db import models


# dados global

class Secretaria(models.Model):
    descricao = models.CharField(max_length=100)
    criado = models.DateField(auto_now_add=True)
    alterado = models.DateField(auto_now=True)

    def __str__(self):
        return self.descricao


class Unidade(models.Model):
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.sigla


class assinante(models.Model):
    nome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    criado = models.DateField(auto_now_add=True)
    alterado = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome


class CentroCusto(models.Model):
    descricao = models.CharField(max_length=100)
    criado = models.DateField(auto_now_add=True)
    alterado = models.DateField(auto_now=True)

    def __str__(self):
        return self.descricao


class Fornecedor(models.Model):
    razao = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=14)
    criado = models.DateField(auto_now_add=True)
    alterado = models.DateField(auto_now=True)

    def __str__(self):
        return self.razao


# dados para requisicao compra direta

class Requerimento(models.Model):
    origem = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    destino = models.ForeignKey(CentroCusto, on_delete=models.CASCADE)
    justificativa = models.TextField()
    criado = models.DateField(auto_now_add=True)
    data = models.DateField()
    
    def __str__(self):
        return self.justificativa


class Assinatura(models.Model):
    assinante = models.ForeignKey(assinante, on_delete=models.CASCADE)
    requerimento = models.ForeignKey(Requerimento, on_delete=models.CASCADE)


class ItemRequerido(models.Model):
    quantidade = models.IntegerField()
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    requerimento = models.ForeignKey(Requerimento, on_delete=models.CASCADE)


# Ata de Registro de Preço (ARP)

class AtaRegistoPreco(models.Model):
    contrato = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    criado = models.DateField(auto_now_add=True)
    alterado = models.DateField(auto_now=True)

    def __str__(self):
        return ' '.join(self.contrato, self.descricao)


class RequerimentoARP(models.Model):
    origem = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    destino = models.ForeignKey(CentroCusto, on_delete=models.CASCADE)
    justificativa = models.TextField()
    criado = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.justificativa


class AssinaturaARP(models.Model):
    assinante = models.ForeignKey(assinante, on_delete=models.CASCADE)
    requerimento = models.ForeignKey(RequerimentoARP, on_delete=models.CASCADE)


class ProdutoARP(models.Model):
    produto = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    fornercedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    arp = models.ForeignKey(AtaRegistoPreco, on_delete=models.CASCADE)


class ItemRequeridoARP(models.Model):
    quantidade = models.DecimalField(max_digits=10, decimal_places=0)
    produtoARP = models.ForeignKey(ProdutoARP, on_delete=models.CASCADE)
    requerimentoARP = models.ForeignKey(RequerimentoARP, on_delete=models.CASCADE)