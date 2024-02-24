from django.urls import path
from .views import add_task, task_add

urlpatterns = [
    path('run/', add_task),
    path('show/<int:pk>/', task_add)
]