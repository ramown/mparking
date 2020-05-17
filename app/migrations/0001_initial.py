# Generated by Django 3.0.6 on 2020-05-17 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('capacidade', models.IntegerField()),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=15)),
                ('tipo', models.IntegerField(choices=[(0, 'CARRO'), (1, 'MOTOCICLETA'), (2, 'VAN'), (3, 'ÔNIBUS')])),
                ('categoria', models.IntegerField(choices=[(0, 'PREFERENCIAL'), (1, 'FUNCIONARIO'), (2, 'ALUNO'), (6, 'VISITANTE')])),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Pessoa')),
                ('matricula', models.CharField(max_length=15)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('app.pessoa',),
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Pessoa')),
                ('tipo', models.IntegerField(choices=[(0, 'ALUNO'), (1, 'PROFESSORES'), (2, 'ADMINISTRATIVO'), (3, 'VISITANTES')])),
            ],
            bases=('app.pessoa',),
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
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_final', models.DateField(blank=True, null=True)),
                ('areas_usadas', models.ManyToManyField(to='app.Area')),
            ],
        ),
        migrations.AddField(
            model_name='veiculo',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Proprietario'),
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(0, 'FURTO'), (1, 'SINISTRO'), (2, 'ESTACIONAMENTO INDEVIDO'), (3, 'AVARIA'), (4, 'INUNDAÇÃO'), (5, 'OUTROS')])),
                ('data_ocorrencia', models.DateField(blank=True, null=True)),
                ('data_registro', models.DateField(auto_now=True)),
                ('descricao', models.TextField()),
                ('funcionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Funcionario')),
            ],
        ),
    ]
