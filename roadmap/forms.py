from django import forms

from .models import Goal


class CustomDateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'deadline']
        widgets = {
            'deadline': CustomDateTimeInput()
        }
