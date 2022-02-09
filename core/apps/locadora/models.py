from pyexpat import model
from unicodedata import decimal
from django.db import models


tipo_pessoa = (
    ('F', 'Física'),
    ('J', 'Jurídica'),
)
class Veiculo(models.Model):
    proprietario = models.CharField(max_length=255, null=False, blank=False, verbose_name='Proprietário', )
    renavam = models.CharField(max_length=100, null=False, blank=False, verbose_name='RENAVAM', )
    placa = models.CharField(max_length=8, null=False, blank=False, )
    chassi = models.CharField(max_length=35, null=False, blank=False, )
    marca = models.CharField(max_length=50, )
    modelo = models.CharField(max_length=50, )
    ano = models.IntegerField()
    valor_locacao = models.DecimalField(max_digits=8, decimal_places=2, )
    data_aquisicao = models.DateField(blank=True, )
    cor = models.CharField(max_length=50, )
    numero_portas = models.IntegerField()
    motor = models.IntegerField()
    cambio = models.CharField(max_length=50, )
    combustivel = models.CharField(max_length=50, )
    nivel_tanque = models.DecimalField(max_digits=2, decimal_places=2, )
    km_atual = models.DecimalField(max_digits=8, decimal_places=2, )
    disponibilidade = models.IntegerField()
    observacao = models.TextField()


class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, )
    razao_social = models.CharField(max_length=255, null=False, blank=False, )
    cpf = models.CharField(max_length=11, null=False, blank=False, )
    rg = models.CharField(max_length=20, )
    dt_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20, )
    celular = models.CharField(max_length=20, )
    endereco = models.CharField(max_length=100, )
    cnh_numero = models.CharField(max_length=30, )
    cnh_numregistro = models.CharField(max_length=30, )
    cnh_validade = models.DateField()
    cnh_categoria = models.CharField(max_length=5, )
    observacao = models.TextField()
    situacao = models.IntegerField()
    cnpj = models.CharField(max_length=15, )
    insc_estadual = models.CharField(max_length=20, )
    insc_municipal = models.CharField(max_length=20, )
    tipo_pessoa = models.CharField(max_length=1, choices=tipo_pessoa, )
    senha = models.CharField(max_length=50, )

    def __str__(self):
        return f'{self.nome}'


class FormPag(models.Model):
    forma = models.CharField(max_length=50, null=False, blank=False, )
    observacao = models.TextField()

    def __str__(self):
        return f'{self.forma}'

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, )
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, )
    datahora_locacao = models.DateTimeField(auto_now_add=True, )
    datahora_prevista_devolucao = models.DateTimeField()
    datahora_devolucao = models.DateTimeField()
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, )
    qtde_dias = models.IntegerField()
    km_devolucao = models.DecimalField(max_digits=8, decimal_places=2, )

    def __str__(self):
        return f'{self.cliente.nome} - {self.veiculo.placa} - {self.veiculo.modelo}'


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, )
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, )
    datahora_reserva = models.DateTimeField(null=False, )

    def __str__(self):
        return f'{self.datahora_reserva} - {self.veiculo.placa} - {self.veiculo.modelo}'