from django.urls import path, include
from .views import HelloView

from . import views

urlpatterns = [
  path("home/", views.welcome, name= "home"),
  path("hello/", HelloView.as_view(), name="hello"),

]