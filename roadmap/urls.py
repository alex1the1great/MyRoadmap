from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/delete/', views.goal_delete, name='goal_delete'),
    path('<slug:slug>/update/', views.goal_update, name='goal_update'),
    path('add/', views.goal_add, name='goal_add'),
    path('', views.goal_list, name='goal_list'),

    path('<slug:slug>/task/add/', views.task_add, name='task_add'),
]
