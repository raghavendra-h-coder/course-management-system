from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from accounts.models import Role
from enrollments.models import Enrollment
from enrollments.permissions import IsAuthenticatedStudent
from enrollments.serializers import EnrollmentReadSerializer, EnrollmentWriteSerializer

class EnrollmentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedStudent]

    def get_queryset(self):
        if self.request.user.role == Role.ADMIN:
            return Enrollment.objects.all()
        return Enrollment.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EnrollmentReadSerializer
        return EnrollmentWriteSerializer

    def create(self, request, *args, **kwargs):
        # Validate request using WriteSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the enrollment
        enrollment = serializer.save()

        # Serialize response using ReadSerializer
        response_serializer = EnrollmentReadSerializer(enrollment)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )

