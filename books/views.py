from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def books(request):
  template = loader.get_template('general/book.html')
  return HttpResponse(template.render())