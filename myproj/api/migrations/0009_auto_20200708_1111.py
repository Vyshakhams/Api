# Generated by Django 2.2.4 on 2020-07-08 05:41

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200708_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name=api.models.ActivityPeriod),
        ),
    ]
