from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('goals/', include('roadmap.urls'))
]
