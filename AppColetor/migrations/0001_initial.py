# Generated by Django 3.0.8 on 2020-07-14 19:55

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
            name='CadastroPessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cracha', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Coletores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coletor', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=15)),
                ('marca', models.CharField(choices=[('mo', 'Motorola'), ('in', 'Intermec')], max_length=30)),
                ('serial_number', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('fo', 'Fornecedor'), ('co', 'Condenado'), ('de', 'Defeito'), ('ma', 'Manutenlção'), ('no', 'Normal')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Controle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtretirada', models.DateTimeField(auto_now_add=True)),
                ('dtentrega', models.DateTimeField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('coletor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppColetor.Coletores')),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppColetor.CadastroPessoa')),
                ('userentrega', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='userentrega', to=settings.AUTH_USER_MODEL)),
                ('userretidada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usercadastro', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]