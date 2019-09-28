from django.urls import path

from monitoring.views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard')
]
