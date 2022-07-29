from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avata = models.ImageField(upload_to='users_dp/')
    tel = models.CharField(max_length=30, blank=True)


class UserVisit(models.Model):
    date_visitad = models.DateField(auto_now_add=True)
    count_users = models.BigIntegerField()


class UserFeedback(models.Model):
    visitor_name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=500)


class Docs(models.Model):
    name = models.CharField(max_length=30)
    doc = models.FileField(upload_to='docs')
    date = models.DateTimeField(auto_now_add=True)
    trainer = models.ForeignKey(User, db_column='trainer', on_delete=models.DO_NOTHING)


class Tag(models.Model):
    tag = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    message = models.TextField(max_length=1000)
    tag = models.ForeignKey(Tag, db_column='tag', on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, db_column='trainer', on_delete=models.DO_NOTHING)


class Response(models.Model):
    response = models.TextField(max_length=1000)
    tag = models.ForeignKey(Tag, db_column='tag', on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, db_column='trainer', on_delete=models.DO_NOTHING)

    