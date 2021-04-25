from django import forms

from .models import Goal, Task


class CustomDateInput(forms.DateTimeInput):
    input_type = 'date'


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'deadline']
        widgets = {
            'deadline': CustomDateInput()
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline']
        widgets = {
            'deadline': CustomDateInput()
        }
