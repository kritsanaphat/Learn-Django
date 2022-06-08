from multiprocessing import context
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

all_book = [
  {'id' : 1,'title': 'Physic','price':200,'is_premium': True },
  {'id' : 2,'title': 'Math','price':150,'is_premium': False },
  {'id' : 3,'title': 'Sport','price':100,'is_premium': False }
]

def book(request,book_id):
  template = loader.get_template('general/book.html')
  return HttpResponse(template.render(context={'book_id':book_id}))

def books(request):
  context = {'books': all_book}
  template = loader.get_template('general/books.html')
  return HttpResponse(template.render(context))


