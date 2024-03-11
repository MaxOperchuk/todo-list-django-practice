from django.urls import path

from .views import (
    IndexListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    complete_task_view,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView
)

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="create-task"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="update-task"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete-task"),
    path("task/<int:pk>/complete/", complete_task_view, name="complete-task"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create", TagCreateView.as_view(), name="create-tag"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="delete-tag"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="update-tag"),
]


app_name = "app_todo_list"
