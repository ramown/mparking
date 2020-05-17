# Generated by Django 3.0.6 on 2020-05-17 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_ocorrencia_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=15)),
                ('tipo', models.IntegerField(choices=[(0, 'CARRO'), (1, 'MOTOCICLETA'), (2, 'VAN'), (3, 'ÔNIBUS')])),
                ('categoria', models.IntegerField(choices=[(0, 'PREFERENCIAL'), (1, 'FUNCIONARIO'), (2, 'ALUNO'), (6, 'VISITANTE')])),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField(blank=True, null=True)),
                ('data_saida', models.DateField(blank=True, null=True)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Area')),
                ('veiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Veiculo')),
            ],
        ),
    ]
