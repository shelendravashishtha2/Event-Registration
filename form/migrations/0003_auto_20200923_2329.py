# Generated by Django 3.0.3 on 2020-09-23 23:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20200923_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 23, 23, 29, 46, 281040)),
        ),
    ]