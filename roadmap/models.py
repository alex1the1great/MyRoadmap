from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Goal(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='created_at')
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')

    def __str__(self):
        return self.title
