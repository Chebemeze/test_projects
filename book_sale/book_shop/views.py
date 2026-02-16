from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .models import Book
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse, Http404
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

class SignupView(CreateView):
  model = Book
  form_class = UserCreationForm
  template_name = "book_shop/create.html"
  success_url = reverse_lazy('home')

# A class based view to update an existing record
# you don't have to specify the context_object_name for CreateView
# and UpdateView because the object name by default is form
# when using CreatView and UpdateView the fields to modify must be specified in the class
class UpdateBookView(UpdateView):
  model = Book
  fields = ('Author', 'title', 'SNB', 'is_available',)
  template_name = "book_shop/create.html"
  success_url= reverse_lazy('all_books')


  def get_object(self, queryset = None):
    try:
      return super().get_object(queryset)
    except Http404:
      return None
    
  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    if self.object is None:
      context = {
        'error_message': "The book you are looking for does not exist, enter a valid pk next time",
      }
      return render (request, 'book_shop/not_found.html', context)
    return super().get(request, *args, **kwargs)


