# Generated by Django 3.2.7 on 2021-09-30 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_delete_revisao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revisao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revisao1', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Primeira Revisão')),
                ('revisao2', models.PositiveIntegerField(blank=True, default=7, null=True, verbose_name='Segunda Revisão')),
                ('revisao3', models.PositiveIntegerField(blank=True, default=14, null=True, verbose_name='Terceira Revisão')),
                ('revisao4', models.PositiveIntegerField(blank=True, default=30, null=True, verbose_name='Quarta Revisão')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Revisão',
                'verbose_name_plural': 'Revisões',
            },
        ),
    ]