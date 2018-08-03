from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.



def get_users(request):#GET
    users = models.User.objects.all()
    s = ""
    for user in users:
        s+=str(user)+"\n"
    return HttpResponse(s)

@csrf_exempt
def add_subscription(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    username = body['username']
    subscription = body['subscription']

    if assert_model_exists(username):
        subscriptions = models.User.objects.get(username=username).subscriptions
        models.User.objects.get(username=username).add_subscription(subscription)
        response = "Success"
    else:
        response = "Model Does Not Exist"

    return HttpResponse(response)
    

@csrf_exempt 
def make_user(request):#POST

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    
    username = body['username']
    password = body['password']
    
    if assert_not_duplicate(username):
        user = models.User(username=username,password=password)
        user.save()
        response = "Success"
    else:
        response = "No Duplicate Usernames"
        
    return HttpResponse(response)

@csrf_exempt 
def delete_user(request):#POST
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']

    if assert_model_exists(username):
        models.User.objects.get(username=username).delete()
        response = "Success"
    else:
        response = "Model Does Not Exist"

    return HttpResponse(response)
    

def assert_model_exists(username):
    users = models.User.objects.all()
    for user in users:
        if user.username == username:
            return True
    return False

def assert_not_duplicate(username):
    users = models.User.objects.all()
    for user in users:
        if user.username == username:
            return False
    return True
