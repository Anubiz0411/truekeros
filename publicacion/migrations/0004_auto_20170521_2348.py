# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0003_auto_20170417_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(permissions=(gdstorage.storage.GoogleDriveFilePermission(gdstorage.storage.GoogleDrivePermissionRole('reader'), gdstorage.storage.GoogleDrivePermissionType('anyone')),)), upload_to='/truekeros/'),
        ),
    ]
