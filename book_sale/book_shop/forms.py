from django import forms
from .models import Book


class BookForm(forms.ModelForm):

  class Meta:
    model = Book
    fields = ['title', 'SNB', 'Author', 'is_available']
    widgets = {
      "title": forms.TextInput(attrs={"class":"input"}),
      "SNB": forms.TextInput(attrs={"class":"input"}),
      "Author": forms.TextInput(attrs={"class":"input"}),
      "is_available": forms.CheckboxInput(attrs={"class":"input"})
    }