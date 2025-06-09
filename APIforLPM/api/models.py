from django.db import models
from django.contrib.auth.models import User

class Module(models.Model):
    name = models.CharField(max_length=255)
    content_url = models.URLField()
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.name

class LearningPath(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return self.title

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'module')