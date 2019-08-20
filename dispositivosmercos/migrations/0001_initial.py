# Generated by Django 2.2 on 2019-08-20 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colaboradoresmercos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.IntegerField(default=False)),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=30)),
                ('numeromodelo', models.CharField(default='NULL', max_length=30)),
                ('versao', models.CharField(max_length=10)),
                ('disponivel', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('ultima_alteracao', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DispositivosColaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_emprestimo', models.DateField()),
                ('data_de_devolucao', models.DateTimeField(null=True)),
                ('ultima_alteracao', models.DateTimeField(null=True)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='colaboradoresmercos.Colaborador')),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dispositivosmercos.Dispositivos')),
            ],
        ),
    ]