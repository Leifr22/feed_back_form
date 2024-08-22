from django.db import models

# Create your models here.
from django.urls import reverse


class Feedback(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    feedback=models.TextField()
    rating=models.PositiveIntegerField()

    def get_url(self):
        return reverse('feedback_details', args=[self.id])

