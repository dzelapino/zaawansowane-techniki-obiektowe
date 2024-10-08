from django.urls import path

from ztoapi.views import TaskListApiView

urlpatterns = [
    path('', TaskListApiView.as_view(), name='task-list')
]
