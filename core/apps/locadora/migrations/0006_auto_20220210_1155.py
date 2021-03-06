# Generated by Django 3.2.9 on 2022-02-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0005_auto_20220209_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': '2. Clientes'},
        ),
        migrations.AlterModelOptions(
            name='formpag',
            options={'verbose_name': 'Forma de Pagamento', 'verbose_name_plural': '3. Formas de Pagamento'},
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name': 'Veículo', 'verbose_name_plural': '1. Veículos'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cnh_categoria',
            field=models.CharField(max_length=5, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cnh_numero',
            field=models.CharField(max_length=30, verbose_name='Número da CNH'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cnh_numregistro',
            field=models.CharField(max_length=30, verbose_name='Núm. Registro da CNH'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cnh_validade',
            field=models.DateField(verbose_name='Válida até'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dt_nascimento',
            field=models.DateField(blank=True, verbose_name='Data Nascimento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(max_length=100, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='insc_estadual',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Insc. Estadual'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='insc_municipal',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Insc. Municipal'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(blank='True', max_length=20, verbose_name='R.G.'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='senha',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='situacao',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_pessoa',
            field=models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], default='F', max_length=1, verbose_name='Tipo do Cliente ( F/J )'),
        ),
        migrations.AlterField(
            model_name='formpag',
            name='forma',
            field=models.CharField(max_length=50, verbose_name='Descrição da Forma de Pagamento'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='ano',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='cambio',
            field=models.CharField(blank=True, max_length=50, verbose_name='Câmbio'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='combustivel',
            field=models.CharField(blank=True, max_length=50, verbose_name='Tipo de combustível'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='cor',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='data_aquisicao',
            field=models.DateField(blank=True, verbose_name='Data de Compra do Veículo'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='km_atual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8),
        ),
    ]
