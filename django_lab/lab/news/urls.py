from django.urls import path

from .views import index, add, get, update, update_record

urlpatterns = [
    path("", index, name="view_news"),
    path("add/", add, name="add"),
    path("<int:id>/", get, name="get"),
    path("update/<int:id>/", update, name="update"),
    path("updaterecord/<int:id>/", update_record, name="updaterecord"),
]
