# Generated by Django 3.0.6 on 2020-05-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200517_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocorrencia',
            name='descricao',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]