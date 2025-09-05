from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TaskListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        '''get all tasks'''
        tasks = task.objects.filter(user=request.user);
        serialzer= TaskSerializer(tasks, many=True)
        return Response(serialzer.data)

    def post(self,request):
        '''create a new task'''
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailAPIView(APIView):
    def get(self, request, pk):
        '''get a task by id'''
        getTask = task.objects.get(pk=pk, user=request.user)
        serializer = TaskSerializer(getTask)
        return Response(serializer.data)
        serializer = TaskSerializer(getTask, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        '''update a task by id'''
        getTask =get_object_or_404(task,pk=pk, user=request.user)
        serializer = TaskSerializer(getTask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        '''delete a task by id'''
        getTask =  get_object_or_404(task,pk=pk, user=request.user)
        getTask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)