# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lote', models.CharField(max_length=5)),
                ('placas', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=25)),
                ('tipo', models.CharField(max_length=15)),
                ('color', models.CharField(max_length=10)),
                ('anio', models.CharField(max_length=4)),
            ],
        ),
    ]
