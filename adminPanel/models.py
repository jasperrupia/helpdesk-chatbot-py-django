from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avata = models.ImageField(upload_to='users_dp/')
    tel = models.CharField(max_length=30, blank=True)


class UserVisit(models.Model):
    date_visitad = models.DateField(auto_now_add=True)
    count_users = models.BigIntegerField()


class UserFeedback(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=1000)