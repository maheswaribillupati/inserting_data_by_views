from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    tn=input('enter tn:')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    return HttpResponse('topic object is inserted')
    

def insert_webpage(request):
    tn=input('enter tn:')
    n=input('enter name:')
    url=input('enter url:')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    Wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=url)[0]
    Wo.save()
    return HttpResponse('webpage object is inserted')

def insert_accessrecord(request):
    tn=input('enter tn:')
    n=input('enter name:')
    url=input('enter url:')
    a=input('enter author:')
    d=input('enter date:')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    Wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=url)[0]
    Wo.save()
    Ao=Accessrecord.objects.get_or_create(name=Wo,author=a,date=d)[0]
    Ao.save()
    return HttpResponse('accessrecord object is inserted')




