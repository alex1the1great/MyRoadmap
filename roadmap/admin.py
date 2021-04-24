from django.contrib import admin

from .models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'deadline']
    list_filter = ['user']
    raw_id_fields = ('user',)
    prepopulated_fields = {'slug': ('title',)}