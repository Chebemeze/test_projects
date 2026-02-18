from django.urls import path, include
from .views import HelloView, BookView, CreateBookView, UpdateBookView, SignupView

from . import views

urlpatterns = [
  path("home/", views.welcome, name= "home"),
  path("hello/", HelloView.as_view(), name="hello"),
  path("all-books/", BookView.as_view(), name = "all_books"),
  path("create-books/", CreateBookView.as_view(), name = "create_book"),
  path("update/<int:pk>/", UpdateBookView.as_view(), name= "update_book"),
  path("sign-up/", SignupView.as_view(), name= "sign_up"),
  path("create/", views.create, name="create"),

]