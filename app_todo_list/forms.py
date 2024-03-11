from django import forms

from app_todo_list.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control",
            }
        ),
        help_text="Select the deadline date and time"
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tag")
