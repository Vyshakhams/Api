# Generated by Django 2.2.4 on 2020-07-08 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200708_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ok',
            name='activity_periods',
        ),
        migrations.AddField(
            model_name='user',
            name='activity_periods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ActivityPeriod'),
        ),
    ]
