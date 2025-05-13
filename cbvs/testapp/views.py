from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView
class BookListView(ListView):
    model=Book
    #template_name='book_list.html'
    #context_object_name='book_list'
# Create your views here.
