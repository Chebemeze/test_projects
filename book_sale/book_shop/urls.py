from django.urls import path, include
from .views import HelloView, BookView

from . import views

urlpatterns = [
  path("home/", views.welcome, name= "home"),
  path("hello/", HelloView.as_view(), name="hello"),
  path("all-books/", BookView.as_view(), name = "all_books")
]