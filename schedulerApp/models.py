from django.db import models

# Create your models here.
class Request(models.Model):
    title = models.CharField(max_length=200)
    scheduledDateTime = models.DateTimeField()
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    def changeStatus(self, newStatus):
        self.status = newStatus
        self.save()