from django.urls import path

from .views import index, add, get

urlpatterns = [
    path("", index, name="view_news"),
    path("add/", add, name="add"),
    path("<int:id>/", get, name="get"),
]
