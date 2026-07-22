from django.db import models

from courses.models import CourseStatus, Course
from profiles.models import BaseModel

class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.DecimalField(max_digits=4, decimal_places=2)
    video_url = models.URLField()
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=CourseStatus.choices,
        default=CourseStatus.DRAFT,
    )
    is_preview = models.BooleanField(default=False)
    order_number = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.course.title} - {self.title}"
