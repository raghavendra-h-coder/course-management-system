from django.db import models

from courses.models import Course
from profiles.models import StudentProfile, BaseModel

# Create your models here.
class Enrollment(BaseModel):
    student = models.ForeignKey(StudentProfile, related_name="enrollments", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="enrollments", on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    last_viewed_date = models.DateField(null=True, blank=True)
    progress_percentage = models.PositiveIntegerField(default=0)
    completed_at = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course'],
                name="unique_enrollment",
            )
        ]
