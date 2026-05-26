from django.db import models

class tablebooking(models.Model):

    username = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)

    booking_date = models.DateField(null=True, blank=True)
    booking_time = models.TimeField(null=True, blank=True)

    message = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username