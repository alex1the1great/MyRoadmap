from django.shortcuts import render, redirect, get_object_or_404
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


@login_required()
def goal_update(request, slug):
    goal = get_object_or_404(Goal, slug=slug)
    form = GoalForm(instance=goal)

    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    return render(request, 'roadmap/goal_update.html', {'form': form})


@login_required()
def goal_delete(request, slug):
    goal = get_object_or_404(Goal, slug=slug)
    goal.delete()
    return redirect('goal_list')


def goal_index(request):
    """
    Display public page to login or signup. If user is authenticated redirect to goal list template.
    """
    if request.user.is_authenticated:
        return redirect('goal_list')
    else:
        return render(request, 'roadmap/goal_index.html')
