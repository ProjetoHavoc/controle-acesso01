# Generated by Django 3.2.9 on 2021-11-10 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_auto_20211110_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitante',
            old_name='resgistrado_por',
            new_name='registrado_por',
        ),
    ]
