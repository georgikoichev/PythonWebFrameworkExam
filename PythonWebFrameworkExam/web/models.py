from django.contrib.auth.models import User
from django.db import models


class Profile(User):
    pass


class Thread(models.Model):
    thread_title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Thread Name',
    )

    thread_text = models.TextField(
        blank=False,
        null=False,
    )

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    thread = models.ForeignKey(Thread, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']


class Calculation(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    operation = models.CharField(max_length=20)
    result = models.FloatField()


class MathFunctions(models.Model):
    num = models.FloatField()
    operation = models.CharField(max_length=20)
    result = models.FloatField()