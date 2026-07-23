from rest_framework import serializers

from courses.models import Course
from enrollments.models import Enrollment
from profiles.models import StudentProfile


class StudentDetailsSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    class Meta:
        model = StudentProfile
        fields = ['id', 'first_name', 'last_name', 'email']

class CourseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description']

class EnrollmentReadSerializer(serializers.ModelSerializer):
    student = StudentDetailsSerializer(read_only=True)
    course = CourseDetailsSerializer(read_only=True)
    class Meta:
        model = Enrollment
        fields = '__all__'

class EnrollmentWriteSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(source='course', queryset=Course.objects.all(), write_only=True)
    class Meta:
        model = Enrollment
        fields = ['course_id']