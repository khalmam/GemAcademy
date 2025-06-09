from django.urls import path
from .views import (
    LearningPathList,
    LearningPathDetail,
    AddModule,
    RemoveModule,
    TrackProgress,
)

urlpatterns = [
    path('learning-paths/', LearningPathList.as_view()),
    path('learning-paths/<int:pk>/', LearningPathDetail.as_view()),
    path('learning-paths/<int:pk>/add-module/', AddModule.as_view()),
    path('learning-paths/<int:pk>/remove-module/', RemoveModule.as_view()),
    path('learning-paths/<int:pk>/progress/', TrackProgress.as_view()),
]
