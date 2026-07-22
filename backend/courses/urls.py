from rest_framework import routers

from courses.views import CourseModelViewSet

router = routers.DefaultRouter()

router.register("", CourseModelViewSet, basename="course")

urlpatterns = router.urls