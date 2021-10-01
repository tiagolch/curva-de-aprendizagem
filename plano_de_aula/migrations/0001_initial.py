# Generated by Django 3.2.7 on 2021-09-26 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0003_alter_revisao_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plano_de_aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('estudo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.estudos', verbose_name='Estudo')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.materias', verbose_name='Materia')),
                ('revisao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastro.revisao', verbose_name='Revisoes')),
            ],
            options={
                'verbose_name': 'Plano de aula',
                'verbose_name_plural': 'Plano de aulas',
            },
        ),
    ]
