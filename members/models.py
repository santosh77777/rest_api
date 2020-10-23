from django.db import models
import pytz
from timezone_field import TimeZoneField
"""
import uuid
"""

# Create your models here.



class Member(models.Model):
	#id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	real_name = models.CharField(max_length=100)
	tz = TimeZoneField(default='Asia/Kolkata')

	def __str__(self):
		return self.real_name


class ActivityPeriod(models.Model):
	member = models.ForeignKey(Member, related_name='activity_period', on_delete=models.CASCADE, null=True)
	start_time = models.CharField(max_length=100)
	end_time = models.CharField(max_length=100)

	def __str__(self):
		return self.member.real_name