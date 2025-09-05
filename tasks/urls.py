from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView
from .auth_views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail')
]
