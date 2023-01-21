from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class user(TimeStampModel):
    username = models.CharField(max_length=30, null=True,blank=True)
    api_id = models.CharField(max_length=255)
    api_hash = models.CharField(max_length=255)
    number = models.CharField(max_length=20)