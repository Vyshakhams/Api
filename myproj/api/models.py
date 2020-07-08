# Create your models here.
from django.db import models


class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class User(models.Model):
    activity_periods = models.ForeignKey(ActivityPeriod, on_delete=models.SET_NULL, null=True)
    id = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=30)
    tz = models.CharField(max_length=60)


class ok(models.Model):
    # activity_periods = models.ForeignKey(ActivityPeriod, on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)