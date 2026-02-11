from django.views.generic import TemplateView
from .models import Book
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
  return HttpResponse("Welcome to this bookshop")

class HelloView(TemplateView):
  model = Book
  template_name = "hello.html"