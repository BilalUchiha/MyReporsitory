# Generated by Django 4.1.2 on 2022-11-19 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('CityList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.city')),
                ('CustomersList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.customer')),
            ],
        ),
    ]