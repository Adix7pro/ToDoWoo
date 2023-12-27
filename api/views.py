from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializer,UserSerializer
from .models import Todo
# Create your views here.
class TodoList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects
    serializer_class = TodoSerializer


class TodoDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class TodoCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CurrentTodoListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.filter(status='CURRENT')
    serializer_class = TodoSerializer

class CompletedTodoListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.filter(status='COMPLETED')
    serializer_class = TodoSerializer













