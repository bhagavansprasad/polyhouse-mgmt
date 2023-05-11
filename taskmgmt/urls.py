from django.urls import path
from . import apis

urlpatterns = [
    path('hello/', apis.hello, name='hello'),
    path('createtask/', apis.create_task, name='create_task'),
]
