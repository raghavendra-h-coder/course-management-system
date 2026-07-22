from rest_framework import serializers

from courses.models import Course
from lessons.models import Lesson
from profiles.models import InstructorProfile


class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstructorProfile
        fields = [
            "id",
            "experience",
        ]

class LessonSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "title",
            "duration",
            "is_preview"
        ]

class CourseWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        exclude = [
            "instructor"
        ]

class CourseReadSerializer(serializers.ModelSerializer):

    instructor = InstructorSerializer(read_only=True)
    lessons = serializers.SerializerMethodField()

    def get_lessons(self, obj):
        lessons = obj.lessons.order_by("order_number")
        return LessonSummarySerializer(
            lessons,
            many=True
        ).data

    class Meta:
        model = Course
        fields = "__all__"

