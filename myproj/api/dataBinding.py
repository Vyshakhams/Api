from rest_framework import serializers
from .models import ok, ActivityPeriod
# from .models import ActivityPeriod


class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ActivityPeriod
        fields = [
            'id',
            'start_time',
            'end_time'
        ]
        read_only_fields = ('activity_periods',)
        # depth = 2


class UserDataBinding(serializers.ModelSerializer):

    # activity_periods = ChoiceSerializer()
    class Meta:
        model = ok
        fields = ('member',)
        depth = 3
