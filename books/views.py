from multiprocessing import context
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


all_book = [
  {'id' : 1,'title': 'Physic','price':200,'is_premium': True },
  {'id' : 2,'title': 'Math','price':150,'is_premium': False },
  {'id' : 3,'title': 'Sport','price':100,'is_premium': False },
  {'id' : 1,'title': 'Physic','price':200,'is_premium': True },
  {'id' : 2,'title': 'Math','price':150,'is_premium': False },
  {'id' : 3,'title': 'Sport','price':100,'is_premium': False },
  {'id' : 1,'title': 'Physic','price':200,'is_premium': True },
  {'id' : 2,'title': 'Math','price':150,'is_premium': False },
  {'id' : 3,'title': 'Sport','price':100,'is_premium': False },
]

def books(request):
  context = {'books': all_book}
  template = loader.get_template('general/books.html')
  return HttpResponse(template.render(context))


def book(request,book_id):
  one_book = [f for f in all_book if f['id'] == book_id][0]
  context = {'book':one_book}
  template = loader.get_template('general/book.html')
  return HttpResponse(template.render(context))

