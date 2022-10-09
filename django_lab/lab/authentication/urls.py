from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import log_in

urlpatterns = [
    path("login/", log_in),
]
