from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    tn= input('enter data')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    return HttpResponse('table inserted')
