# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 16:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ro_app', '0005_notice_description_for_link_to_site_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarifconnecttechnology',
            old_name='title',
            new_name='name',
        ),
    ]
