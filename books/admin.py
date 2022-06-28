from django.contrib import admin

from books.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'special_price','is_premium']
    search_fields =  ['title']
    list_filter = ['is_premium']


admin.site.register(Book,BookAdmin)

