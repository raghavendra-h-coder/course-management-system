from rest_framework import routers

from lessons.views import LessonModelViewSet

router = routers.DefaultRouter()

router.register("", LessonModelViewSet, basename="lesson")

urlpatterns = router.urls