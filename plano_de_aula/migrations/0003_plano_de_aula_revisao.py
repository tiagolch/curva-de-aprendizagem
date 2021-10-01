# Generated by Django 3.2.7 on 2021-09-26 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_alter_revisao_options'),
        ('plano_de_aula', '0002_remove_plano_de_aula_revisao'),
    ]

    operations = [
        migrations.AddField(
            model_name='plano_de_aula',
            name='revisao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='cadastro.revisao'),
            preserve_default=False,
        ),
    ]
