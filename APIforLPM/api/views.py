from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Module, LearningPath, Progress
from .serializers import ModuleSerializer, LearningPathSerializer, ProgressSerializer
from django.utils.timezone import now

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class LearningPathViewSet(viewsets.ModelViewSet):
    queryset = LearningPath.objects.all()
    serializer_class = LearningPathSerializer

    @action(detail=True, methods=['post'])
    def add_module(self, request, pk=None):
        path = self.get_object()
        module_id = request.data.get('module_id')
        try:
            module = Module.objects.get(id=module_id)
            path.modules.add(module)
            return Response({'status': 'module added'})
        except Module.DoesNotExist:
            return Response({'error': 'Module not found'}, status=404)

    @action(detail=True, methods=['delete'], url_path='remove-module/(?P<module_id>[^/.]+)')
    def remove_module(self, request, pk=None, module_id=None):
        path = self.get_object()
        try:
            module = Module.objects.get(id=module_id)
            path.modules.remove(module)
            return Response({'status': 'module removed'})
        except Module.DoesNotExist:
            return Response({'error': 'Module not found'}, status=404)

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, completed=True, completed_at=now())