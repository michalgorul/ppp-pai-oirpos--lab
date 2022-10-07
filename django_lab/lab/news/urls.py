from django.urls import path

from .views import view_news, add

urlpatterns = [
    path("", view_news, name="index"),
    path("add/", add, name="add"),
]
