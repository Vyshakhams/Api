# Generated by Django 2.2.4 on 2020-07-07 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='first',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
    ]
