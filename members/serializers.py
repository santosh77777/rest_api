from rest_framework import serializers
from .models import Member, ActivityPeriod
from timezone_field import TimeZoneField



class ActivityPeriodSerializer(serializers.ModelSerializer):

     class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']
        read_only_fields = ['start_time', 'end_time']



class MemberSerializer(serializers.ModelSerializer):
     activity_period = ActivityPeriodSerializer(many=True, read_only=True, write_only=False)
     tz = serializers.CharField()

     class Meta:
        model = Member
        fields = ['id', 'real_name', 'tz', 'activity_period']
        extra_kwargs = {'activity_period': {'required': False}}


      

     

        