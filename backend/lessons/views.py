from rest_framework import viewsets

from lessons.models import Lesson
from lessons.permissions import IsInstructorOrReadOnly
from lessons.serializers import LessonReadSerializer, LessonWriteSerializer

class LessonModelViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = [IsInstructorOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LessonReadSerializer
        return LessonWriteSerializer

