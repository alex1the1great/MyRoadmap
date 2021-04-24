from django.shortcuts import render
from django.utils import timezone

from .models import Goal


def goal_list(request):
    goals = Goal.objects.all()
    today_date = timezone.now()
    return render(request, 'roadmap/goal_list.html', {'goals': goals, 'today_date': today_date})
