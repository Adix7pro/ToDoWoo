from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Todo

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


