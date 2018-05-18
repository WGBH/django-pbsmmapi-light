# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PBSMMSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text=b'Not set by API', verbose_name='Created On')),
                ('object_id', models.UUIDField(blank=True, null=True, unique=True, verbose_name='Object ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('publish_status', models.PositiveIntegerField(choices=[(0, b'NOT AVAIL.'), (1, b'AVAILABLE')], default=0, verbose_name='Publish Status')),
                ('api_endpoint', models.URLField(blank=True, help_text=b'Endpoint to original record from the API', null=True, verbose_name='API Endpoint')),
                ('title_sortable', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sortable Title')),
                ('date_last_api_update', models.DateTimeField(help_text=b'Not set by API', null=True, verbose_name='Last API Retrieval')),
                ('ingest_on_save', models.BooleanField(default=False, help_text=b'If true, then will update values from the PBSMM API on save()', verbose_name='Ingest on Save')),
                ('last_api_status', models.PositiveIntegerField(blank=True, null=True, verbose_name='Last API Status')),
                ('json', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='JSON')),
                ('ordinal', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ordinal')),
                ('ingest_episodes', models.BooleanField(default=False, help_text='Also ingest all Episodes (for each Season)', verbose_name='Ingest Epiaodes')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='show.PBSMMShow')),
            ],
            options={
                'db_table': 'pbsmm_season',
                'verbose_name': 'PBS Media Manager Season',
                'verbose_name_plural': 'PBS Media Manager Seasons',
            },
        ),
    ]
