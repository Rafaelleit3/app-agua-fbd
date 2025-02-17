from django.db import models

class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    cargo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Entregador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=100)
    linha = models.CharField(max_length=100)
    unidade = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class ListaPedidos(models.Model):
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return str(self.id)

class ProdutosContidos(models.Model):
    id_lista_pedidos = models.ForeignKey(ListaPedidos, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"Pedido: {self.id_lista_pedidos}, Produto: {self.id_produto}"

class Cupom(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.DateField()
    id_lista_pedidos = models.ForeignKey(ListaPedidos, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_solicitacao = models.DateField()
    hora_solicitacao = models.TimeField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE)
    id_cupom = models.ForeignKey(Cupom, on_delete=models.CASCADE, null=True, blank=True)
    id_lista_pedidos = models.ForeignKey(ListaPedidos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
