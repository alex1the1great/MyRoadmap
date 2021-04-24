from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError

User = settings.AUTH_USER_MODEL


def validate_deadline_is_not_past(value):
    if not value >= timezone.now():
        raise ValidationError('Deadline should be in future date.')


class Goal(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='created_at')
    deadline = models.DateTimeField(default=timezone.now, validators=[validate_deadline_is_not_past])
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField(default=timezone.now, validators=[validate_deadline_is_not_past])

    parent_goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
