# Generated by Django 3.0.8 on 2020-07-30 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppColetor', '0002_auto_20200727_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controle',
            old_name='userretidada',
            new_name='userretirada',
        ),
    ]
