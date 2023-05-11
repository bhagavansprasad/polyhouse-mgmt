from django.http import HttpResponse
from django.http import HttpResponseBadRequest
import json
from taskmgmt.models import Person
from pymongo import MongoClient
import taskmgmt.db_operations as db_operations
import os


def add_to_db(name, age):
    obj1 = db_operations.database()
    
    obj1.create_task(name, age)
    

def hello(request):
    return HttpResponse("Hello, World!\n")

def create_task(request):
    
    try:
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name', 'Unknown')
        age = data.get('age', 0)

        db_obj = db_operations.database()
        db_obj.create_task(name, age)
        
        return HttpResponse(f"Hello, {name}! You are {age} years old.\n")
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON data")

