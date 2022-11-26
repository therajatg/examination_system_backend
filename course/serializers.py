from .models import Test
from rest_framework import serializers

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Test
		fields="__all__"
