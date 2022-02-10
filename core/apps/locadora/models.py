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
    valor_locacao = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor da Locação')
    data_aquisicao = models.DateField(blank=True, verbose_name='Data de Aquisição do Veículo', )
    cor = models.CharField(max_length=50, )
    numero_portas = models.IntegerField(default=2, verbose_name='Número de Portas', )
    motor = models.IntegerField(default=1, )
    cambio = models.CharField(max_length=50, verbose_name='Câmbio')
    combustivel = models.CharField(max_length=50, verbose_name='Tipo de combustível', )
    nivel_tanque = models.DecimalField(max_digits=2, decimal_places=2, default=0.00, verbose_name='Nível do Tanque', )
    km_atual = models.DecimalField(max_digits=8, decimal_places=2, )
    disponibilidade = models.IntegerField(default=1, )
    observacao = models.TextField(blank=True, verbose_name='Observação',)

    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.placa}'


class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, )
    razao_social = models.CharField(max_length=255, null=True, blank=False, )
    cpf = models.CharField(max_length=11, null=True, blank=False, )
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
    observacao = models.TextField(null=True, )
    situacao = models.IntegerField()
    cnpj = models.CharField(max_length=15, null=True, )
    insc_estadual = models.CharField(max_length=20, null=True, )
    insc_municipal = models.CharField(max_length=20, null=True, )
    tipo_pessoa = models.CharField(max_length=1, choices=tipo_pessoa, )
    senha = models.CharField(max_length=50, null=True, )

    def __str__(self):
        return f'{self.nome}'


class FormPag(models.Model):
    forma = models.CharField(max_length=50, null=False, blank=False, verbose_name='Descrição da Forma de Pag.:', )
    observacao = models.TextField(blank=True, verbose_name='Observação', )

    class Meta:
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamento'

    def __str__(self):
        return f'{self.name}'

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Nome do Cliente', )
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veículo', )
    datahora_locacao = models.DateTimeField(auto_now_add=True, verbose_name='Data / Hora da Locação', )
    datahora_prevista_devolucao = models.DateTimeField(verbose_name='Data / Hora prevista p/ Devolução', )
    datahora_devolucao = models.DateTimeField(verbose_name='Data / Hora da Devolução', )
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor Total R$', )
    qtde_dias = models.IntegerField(verbose_name='Qtde. dias locados', )
    km_devolucao = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Anotação de KM do veículo', )

    class Meta:
        verbose_name = 'Locação'
        verbose_name_plural = 'Locações'

    def __str__(self):
        return f'{self.cliente.nome} - {self.veiculo.placa} - {self.veiculo.modelo}'


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, )
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, )
    datahora_reserva = models.DateTimeField(null=False, )

    def __str__(self):
        return f'{self.datahora_reserva} - {self.veiculo.placa} - {self.veiculo.modelo}'