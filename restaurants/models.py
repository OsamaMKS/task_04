from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time =models.TimeField()

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Opening Time: {self.opening_time}, Closing Time: {self.closing_time} "
