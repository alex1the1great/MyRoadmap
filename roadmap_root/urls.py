from django.contrib import admin
from django.urls import path, include

from roadmap.views import goal_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('goals/', include('roadmap.urls')),
    path('', goal_index, name='goal_index')
]
