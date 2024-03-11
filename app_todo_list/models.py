from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    boolean = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="tasks")
