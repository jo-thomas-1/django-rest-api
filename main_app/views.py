from django.shortcuts import render
from rest_framework import viewsets
from . serializers import TaskSerializers, UserSerializers
from . models import Task
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

# Create your views here.
class TaskViewset(viewsets.ModelViewSet):
	permission_class = IsAuthenticated
	queryset = Task.objects.all().order_by('date_created')
	serializer_class = TaskSerializers

class DueTaskViewset(viewsets.ModelViewSet):
	queryset = Task.objects.filter(completed=False).order_by('date_created')
	serializer_class = TaskSerializers

class CompletedTaskViewset(viewsets.ModelViewSet):
	queryset = Task.objects.filter(completed=True).order_by('date_created')
	serializer_class = TaskSerializers

class CreateUserView(CreateAPIView):
	model = get_user_model()
	permission_class = IsAuthenticated
	serializer_class = UserSerializers