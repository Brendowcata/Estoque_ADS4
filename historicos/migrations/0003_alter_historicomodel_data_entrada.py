# Generated by Django 3.2.8 on 2021-11-09 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historicos', '0002_historicomodel_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicomodel',
            name='data_entrada',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
