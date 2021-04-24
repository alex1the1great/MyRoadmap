from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from .models import Goal
from .forms import GoalForm


@login_required()
def goal_list(request):
    goals = Goal.objects.all()
    today_date = timezone.now()
    return render(request, 'roadmap/goal_list.html', {'goals': goals, 'today_date': today_date})


@login_required()
def goal_add(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.slug = slugify(form.cleaned_data['title'])
            goal.user = request.user
            goal.save()
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'roadmap/goal_add.html', {'form': form})
