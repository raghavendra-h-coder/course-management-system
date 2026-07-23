from rest_framework import viewsets, permissions

from accounts.models import Role
from enrollments.models import Enrollment
from enrollments.permissions import IsAuthenticatedStudent
from enrollments.serializers import EnrollmentReadSerializer, EnrollmentWriteSerializer

class EnrollmentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedStudent]

    def get_queryset(self):
        """
        Students can only view their own enrollments.
        Admins can view all enrollments.
        """

        if self.request.user.role == Role.ADMIN:
            return Enrollment.objects.all()

        return Enrollment.objects.filter(
            student=self.request.user.studentprofile
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EnrollmentReadSerializer
        return EnrollmentWriteSerializer

    def perform_create(self, serializer):
        serializer.save(
            student=self.request.user.studentprofile
        )

