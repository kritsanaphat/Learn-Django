from cProfile import label
from dataclasses import field
import re
from tkinter import Widget
import django
from django import forms
from pkg_resources import require
from books.models import Book
from .models import Members

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

class subscriptionModel_form(forms.ModelForm):
    book_set = forms.ModelMultipleChoiceField(
            queryset=Book.objects.order_by('-is_premium'), 
            required=True, 
            label='หนังสือที่สนใจ', 
            widget = forms.CheckboxSelectMultiple
            )
    accepted = forms.BooleanField(required=True,label='ยอมรับข้อตกลงก่อนลงทะเบียน')
    class Meta:
            model = Members
            fields = ['firstname', 'lastname', 'email', 'book_set']
            labels = {
                'firstname': 'ชื่อ',
                'lastname': 'นามสกุล',
                'email': 'อีเมลล์',
                'book_set': 'หนังสือที่สนใจ',
            }
            

