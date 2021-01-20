# Generated by Django 3.1.5 on 2021-01-20 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0005_pontosturisticos_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='Endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
            preserve_default=False,
        ),
    ]
