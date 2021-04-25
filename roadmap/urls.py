from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/update/', views.goal_update, name='goal_update'),
    path('add/', views.goal_add, name='goal_add'),
    path('', views.goal_list, name='goal_list'),
]
