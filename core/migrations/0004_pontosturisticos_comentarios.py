# Generated by Django 3.1.5 on 2021-01-20 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0003_pontosturisticos_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='Comentarios',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]
