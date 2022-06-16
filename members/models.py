from atexit import register
import email
from django.db import models

class Members(models.Model):
  STATUS = [
    ('unapproved','Unapproved'),
    ('approved','Approved'),
    ('banned','Banned')
  ]

  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(max_length=60,unique=True,null=True)
  status = models.CharField(max_length=15,choices=STATUS,default='unapproved')
  register_at = models.DateTimeField(auto_now_add=True,null=True)
  
  #book = models.OneToOneField('books.Book',on_delete=models.SET_NULL,null=True)  -- One to One
  #book = models.ForeignKey('books.Book',on_delete=models.SET_NULL,null=True) --One to Many (user สามารถเลือกหนังสือซ้ำกันได้ แต่เลือกได้แค่คนละเล่ม)
  book_set = models.ManyToManyField('books.Book') #many to many