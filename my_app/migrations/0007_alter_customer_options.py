# Generated by Django 4.1.2 on 2022-11-21 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_delete_customercity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': False, 'ordering': ['address']},
        ),
    ]