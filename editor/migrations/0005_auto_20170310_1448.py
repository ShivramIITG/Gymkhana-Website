# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-10 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0004_auto_20170310_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs',
            name='car_pic1',
            field=models.ImageField(default='pic_folder/no-img.jpg', upload_to='pic_folder/'),
        ),
        migrations.AddField(
            model_name='clubs',
            name='car_pic2',
            field=models.ImageField(default='pic_folder/no-img.jpg', upload_to='pic_folder/'),
        ),
        migrations.AddField(
            model_name='clubs',
            name='car_pic3',
            field=models.ImageField(default='pic_folder/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]