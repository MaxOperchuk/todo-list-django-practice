from django.urls import path

from .views import index

urlpatterns = [
    path("", index, name="index"),
]


app_name = "app_todo_list"
