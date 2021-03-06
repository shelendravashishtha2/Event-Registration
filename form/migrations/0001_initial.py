# Generated by Django 3.0.3 on 2020-09-21 15:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=50)),
                ('current_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('roll_no', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=200)),
                ('suggestion', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('abbr', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('current_status', models.BooleanField(default=True)),
                ('event_code', models.CharField(max_length=10)),
                ('event_venue', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('drive_link', models.CharField(blank=True, max_length=300)),
                ('winner', models.CharField(blank=True, max_length=250)),
                ('first_runner', models.CharField(blank=True, max_length=250)),
                ('second_runner', models.CharField(blank=True, max_length=250)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 9, 21, 15, 26, 25, 395403))),
                ('warn', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=70)),
                ('mobile_number', models.CharField(max_length=10)),
                ('roll_no', models.CharField(max_length=15)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Branch')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Event')),
            ],
        ),
    ]
