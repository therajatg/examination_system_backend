from .models import Course
from rest_framework import serializers

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Course
		fields="__all__"
