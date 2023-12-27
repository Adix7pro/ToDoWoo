from django.urls import path
from .views import *

urlpatterns = [
    path('',TodoList.as_view()),
    path('<int:pk>/',TodoDetail.as_view()),
    path('users/',UserList.as_view()),
    path('current/', CurrentTodoListView.as_view(), name='current_todos'),
    path('completed/', CompletedTodoListView.as_view(), name='completed_todos'),
    path('create/', TodoCreate.as_view())
]