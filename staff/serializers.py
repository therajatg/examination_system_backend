from .models import Staff
from rest_framework import serializers

class StaffSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Staff
		fields="__all__"
