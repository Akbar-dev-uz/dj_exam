from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(choices=[("low", "Past"), ("medium", "O‘rta"), ("high", "Yuqori")], default="medium")

    def __str__(self):
        return self.title

