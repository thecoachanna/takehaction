from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    disability_name = models.CharField(max_length=50, default="")
    disability_description = models.TextField(max_length=1000, default="")
    # disability_message = models.FileField()


class EmergencyContact(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    user = models.ForeignKey(
        "User",
        related_name="emergency_contacts",
        related_query_name="emergency_contact",
        on_delete=models.SET_NULL,
        null=True,
    )
