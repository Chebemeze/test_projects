from django.views.generic import TemplateView, ListView, CreateView
from .models import Book
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
  return HttpResponse("Welcome to this bookshop")

class HelloView(TemplateView):
  template_name = "book_shop/hello.html"

#  adding a list view class
class BookView(ListView):
  model = Book
  template_name= "book_shop/hello.html"
  context_object_name = "book_list"

# This view creates a record
class CreateBookView(CreateView):
  model = Book
  fields = ('Author', 'title', 'SNB', 'is_available',)
  template_name = "book_shop/create.html"
  success_url = reverse_lazy('home')
