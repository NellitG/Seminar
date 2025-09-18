from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()

    title = models.CharField(max_length=200)
    purpose = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    expected_attendees = models.IntegerField()

    audio_visual = models.BooleanField(default=False)
    break_tea = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date} ({self.department})"