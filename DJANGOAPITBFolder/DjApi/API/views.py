from django.shortcuts import render,get_object_or_404
from .models import Task
from rest_framework.response import Response
from .serializer import TaskSerializer
from rest_framework.decorators import api_view



@api_view(http_method_names=['GET','POST'])
def add_task(request):
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(data=serializer.data)






@api_view(http_method_names=['GET','PUT','PATCH','DELETE'])
def task_add(request, pk=None):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(data=serializer.data)

    if request.method == "DELETE":
        task.delete()
        return Response(data=None, status=204)

    if request.method == "PUT":
        serializer = TaskSerializer(data=request.data, instance=task)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)

    if request.method == "PATCH":
        serializer = TaskSerializer(data=request.data, instance=task, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)



