from django.contrib import admin
from .models import Veiculo, Cliente, Locacao, Reserva

admin.site.register(Veiculo)
admin.site.register(Cliente)
admin.site.register(Locacao)
admin.site.register(Reserva)


# Register your models here.
