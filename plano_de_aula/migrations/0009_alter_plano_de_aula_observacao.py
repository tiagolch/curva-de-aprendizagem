# Generated by Django 3.2.7 on 2021-09-30 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plano_de_aula', '0008_auto_20210930_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano_de_aula',
            name='observacao',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observação'),
        ),
    ]
