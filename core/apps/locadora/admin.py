from inspect import formatargspec
from django.contrib import admin
from .models import Veiculo, Cliente, Locacao, Reserva, FormPag

admin.site.register(Veiculo)
admin.site.register(Cliente)
admin.site.register(Locacao)
admin.site.register(Reserva)
admin.site.register(FormPag)


# Register your models here.
