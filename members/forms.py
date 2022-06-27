from cProfile import label
import re
from tkinter import Widget
import django
from django import forms
from pkg_resources import require
from books.models import Book

# class BookMultipleChoiceField(forms.ModelMultipleChoiceField):
#     def lable_from_instance(self, obj):
#         return obj.Book.price                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        


class subscription_form(forms.Form):
    firstname = forms.CharField(max_length=255, required=True, label='ชื่อ')
    lastname = forms.CharField(max_length=255, required=True, label='นามสกุล')
    email = forms.EmailField(max_length=60, required=True, label='อีเมลล์')
    book_set = forms.ModelMultipleChoiceField(
        queryset=Book.objects.order_by('-is_premium'), 
        required=True, 
        label='หนังสือที่สนใจ', 
        widget = forms.CheckboxSelectMultiple
    )
    accepted = forms.BooleanField(required=True,label='ยอมรับข้อตกลง')