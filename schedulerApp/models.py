from django.db import models

# Create your models here.
class Request(models.Model):
    description = models.CharField(max_length=200)
    scheduledDateTime = models.DateTimeField()
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.description
    def changeStatus(self, newStatus):
        self.status = newStatus
        self.save()