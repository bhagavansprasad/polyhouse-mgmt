# polyhouse-mgmt
polyhouse-mgmt

# Data base name
polyhouse

# collection name
taskmgmt

# django Hello world
```commands
pip install Django

django-admin startproject myproject
python manage.py startapp myapp

server.py
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]

from django.urls import include, path

urlpatterns = [
    path('', include('myapp.urls')),
]

python manage.py runserver

http://127.0.0.1:8000/hello/
```


# how to run
```commands
curl http://127.0.0.1:8000/hello/ 
curl -X POST http://127.0.0.1:8000/createtask/ -H "Content-Type: application/json" -d '{"name": "John", "age": 30}'
```

# how to test
```commands
python manage.py test
```