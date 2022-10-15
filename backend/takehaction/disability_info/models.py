from django.db import models
from django.contrib.auth.models import AbstractUser


class DisabilityInfo(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)


class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    disability_info = models.OneToOneField(
        DisabilityInfo, on_delete=models.SET_NULL, null=True
    )


class EmergencyContact(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
