from django.core import validators
from django.db import models


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