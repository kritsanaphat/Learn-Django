from multiprocessing import context
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from datetime import datetime


from .models import Book
all_book = Book.objects.order_by('-is_premium')

def books(request):
  context = {'books': all_book}
  template = loader.get_template('general/books.html')
  return HttpResponse(template.render(context))


def book(request, book_id):
  one_book = None
  try:
    one_book = Book.objects.get(id=book_id)
  except:
    print("ไม่พบหนังสือ")
  # try:
  #   one_book = [f for f in all_book if f['id'] == book_id][0]
  # except IndexError:
  #   print("ไม่พบข้อมูล")

  context = {'book':one_book}
  template = loader.get_template('general/book.html')
  return HttpResponse(template.render(context))

