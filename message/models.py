
from django.db import models

# Create your models here.


class Message(models.Model):
    userName = models.CharField(max_length=250, blank=False, null=False)
    userEmail = models.EmailField(max_length=100, blank=False, null=False)
    subject = models.TextField(max_length=800,  blank=False, null=False)
    message = models.TextField(max_length=1000, blank=False, null=False)


    def __str__(self):
        return self.userName