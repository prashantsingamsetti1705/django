from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
class BookListView(ListView):
    model=Book
    #template_name='book_list.html'
    #context_object_name='book_list'
class BookListView2(ListView):
    model=Book
    template_name='testapp/booklist.html'
    context_object_name='booklist'
class DetailView(DetailView):
    model=Book
    # template_name='testapp/detaillist.html'
    # context_object_name='detaillist'
class CreateView(CreateView):
    model=Book
    fields=['title','author','pages','price']
class UpdateView(UpdateView):
    model=Book
    fields='__all__'
from django.urls import reverse_lazy
class DeleteView(DeleteView):
    model=Book
    success_url=reverse_lazy('book_list')
# Create your views here.
