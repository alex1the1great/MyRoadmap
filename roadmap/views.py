from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Goal


@login_required()
def goal_list(request):
    goals = Goal.objects.all()
    today_date = timezone.now()
    return render(request, 'roadmap/goal_list.html', {'goals': goals, 'today_date': today_date})
