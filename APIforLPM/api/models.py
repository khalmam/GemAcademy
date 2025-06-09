from django.db import models

class Module(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class LearningPath(models.Model):
    name = models.CharField(max_length=100)
    modules = models.ManyToManyField(Module, blank=True)
    progress = models.FloatField(default=0.0)  # percentage (0-100)

    def __str__(self):
        return self.name
