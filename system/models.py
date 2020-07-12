from django.contrib.auth.models import User
from django.db import models


class Employee(User):
    role = models.CharField(max_length=255)
