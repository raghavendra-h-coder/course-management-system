from rest_framework import routers

from enrollments.views import EnrollmentModelViewSet

router = routers.DefaultRouter()

router.register('', EnrollmentModelViewSet, basename='enrollments')

urlpatterns = router.urls