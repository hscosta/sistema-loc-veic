# Generated by Django 3.2.9 on 2022-02-09 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fila',
            new_name='Reserva',
        ),
    ]
