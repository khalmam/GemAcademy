from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LearningPath, Module
from .serializers import LearningPathSerializer

class LearningPathList(APIView):
    def get(self, request):
        paths = LearningPath.objects.all()
        serializer = LearningPathSerializer(paths, many=True)
        return Response(serializer.data)

class LearningPathDetail(APIView):
    def get(self, request, pk):
        try:
            path = LearningPath.objects.get(pk=pk)
            serializer = LearningPathSerializer(path)
            return Response(serializer.data)
        except LearningPath.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

class AddModule(APIView):
    def post(self, request, pk):
        try:
            path = LearningPath.objects.get(pk=pk)
            module_id = request.data.get("module_id")
            module = Module.objects.get(id=module_id)
            path.modules.add(module)
            path.save()
            return Response({"message": "Module added."})
        except Exception as e:
            return Response({"error": str(e)}, status=400)

class RemoveModule(APIView):
    def post(self, request, pk):
        try:
            path = LearningPath.objects.get(pk=pk)
            module_id = request.data.get("module_id")
            module = Module.objects.get(id=module_id)
            path.modules.remove(module)
            path.save()
            return Response({"message": "Module removed."})
        except Exception as e:
            return Response({"error": str(e)}, status=400)

class TrackProgress(APIView):
    def post(self, request, pk):
        try:
            path = LearningPath.objects.get(pk=pk)
            progress = request.data.get("progress")
            path.progress = progress
            path.save()
            return Response({"message": "Progress updated."})
        except Exception as e:
            return Response({"error": str(e)}, status=400)
