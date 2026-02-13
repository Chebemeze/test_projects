from django.views.generic import TemplateView, ListView
from .models import Book
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

