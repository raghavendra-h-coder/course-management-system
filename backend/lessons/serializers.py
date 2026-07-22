from rest_framework import serializers

from courses.models import Course
from lessons.models import Lesson

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description'
        ]

class LessonReadSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = "__all__"

class LessonWriteSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', write_only=True)
    class Meta:
        model = Lesson
        exclude = ['course']
