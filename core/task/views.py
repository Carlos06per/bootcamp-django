from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import task
from .serializer import TaskSerializer
from rest_framework import generics
# Create your views here.
class GetTask(generics.ListAPIView):
    queryset = task.objects.all()
    serializer_class = TaskSerializer
    