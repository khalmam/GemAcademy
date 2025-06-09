# your_app_name/admin.py
from django.contrib import admin
from .models import Module, LearningPath

admin.site.register(Module)
admin.site.register(LearningPath)