from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    boolean = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["datetime"]
