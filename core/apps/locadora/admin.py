from inspect import formatargspec
from django.contrib import admin
from .models import Veiculo, Cliente, Locacao, Reserva, FormPag

# admin.site.register(Veiculo)
# admin.site.register(Cliente)
# admin.site.register(Locacao)
# admin.site.register(Reserva)
# admin.site.register(FormPag)

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    fields = (
        ('proprietario', 'renavam'), 
        ('placa', 'chassi'), 
        ('marca', 'modelo', 'ano', 'data_aquisicao'),
        ('cor', 'numero_portas', 'motor', 'cambio'),
        ('valor_locacao'),
        ('combustivel', 'nivel_tanque'),
        ('km_atual', 'disponibilidade'),
        ('observacao'),
    )

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    fields = (
        ('tipo_pessoa'),
        ('nome'),
        ('cpf', 'rg', 'dt_nascimento'),
        ('email'),
        ('telefone', 'celular'),
        ('endereco'),
        ('cnh_numero', 'cnh_numregistro', 'cnh_validade', 'cnh_categoria'),
        ('observacao', 'situacao'),
        ('cnpj', 'insc_estadual', 'insc_municipal'),
        ('senha'),
    )

@admin.register(FormPag)
class FormPagAdmin(admin.ModelAdmin):
    fields = (
        (),
        (),
        (),
    )