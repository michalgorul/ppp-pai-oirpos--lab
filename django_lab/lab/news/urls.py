from django.urls import path

from .views import view_news

urlpatterns = [
    path("", view_news),
]
