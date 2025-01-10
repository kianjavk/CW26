from django.db import models

# Create your models here.
class TimeDestination(models.Model):
    name = models.CharField(max_length=120,unique=True)
    description = models.TextField()
    origin = models.CharField(max_length=120)
    destination = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'time_destinations'


