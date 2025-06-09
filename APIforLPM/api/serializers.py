from rest_framework import serializers
from .models import Module, LearningPath

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class LearningPathSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = LearningPath
        fields = ['id', 'name', 'modules', 'progress']
