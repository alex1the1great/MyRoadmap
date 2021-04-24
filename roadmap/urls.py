from django.urls import path

from . import views

urlpatterns = [
    path('goal/add/', views.goal_add, name='goal_add'),
    path('', views.goal_list, name='goal_list'),
]
