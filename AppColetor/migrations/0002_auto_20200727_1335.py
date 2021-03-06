# Generated by Django 3.0.8 on 2020-07-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppColetor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coletores',
            name='marca',
            field=models.CharField(choices=[('mo', 'Motorola'), ('in', 'Intermec'), ('ro', 'Honeywell')], max_length=30),
        ),
        migrations.AlterField(
            model_name='coletores',
            name='status',
            field=models.CharField(choices=[('fo', 'Fornecedor'), ('co', 'Condenado'), ('de', 'Defeito'), ('ma', 'Manutenção'), ('no', 'Normal')], max_length=30),
        ),
    ]
