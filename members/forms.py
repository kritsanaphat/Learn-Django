from cProfile import label
from tkinter import Widget
import django
from django import forms
from pkg_resources import require
from books.models import Book

class subscription_form(forms.Form):
    fristname = forms.CharField(max_length=255, required=True, label='ชื่อ')
    lasttname = forms.CharField(max_length=255, required=True, label='นามสกุล')
    email = forms.EmailField(max_length=60, required=True, label='อีเมลล์')
    book_set = forms.ModelMultipleChoiceField(queryset=Book.objects.order_by('-is_premium'), 
        required=True, label='หนังสือที่สนใจ', widget = forms.CheckboxSelectMultiple)
    accepted = forms.BooleanField(required=True,label='ยอมรับข้อตกลง')