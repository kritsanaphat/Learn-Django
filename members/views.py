# from django.shortcuts import render

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello world!")
#-------------------
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse


def home(request):
  template = loader.get_template('general/myfirst.html')
  return HttpResponse(template.render())
  
def about(requset):
  template = loader.get_template('general/about.html')
  return HttpResponse(template.render())

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('general/index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('general/add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('general/index'))

def id(requset,id):
  return HttpResponse('ชื่อผู้ใช้งาน = '+str(id))