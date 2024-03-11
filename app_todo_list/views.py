from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from app_todo_list.forms import TaskForm
from app_todo_list.models import Task


class IndexListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().order_by("boolean")
    template_name = "app_todo_list/index.html"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app_todo_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app_todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app_todo_list:index")


def complete_task_view(request: HttpRequest, pk: int):
    task = Task.objects.get(pk=pk)
    task.boolean = not task.boolean
    task.save()
    return HttpResponseRedirect(reverse_lazy("app_todo_list:index"))
