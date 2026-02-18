from django.forms import forms
from .models import Book


class BookModel(forms.ModelForm):

  class meta:
    model = Book
    fields = ['title', 'SNB', 'Author', 'is-available']
    widget = {
      "title": forms.CheckboxInput(attrs={"class":"input"}),
      "SNB": forms.TextInput(attrs={"class":"input"}),
      "Author": forms.TextInput(attrs={"class":"input"}),
      "is_available": forms.CheckboxInput(attrs={"class":"input"})
    }