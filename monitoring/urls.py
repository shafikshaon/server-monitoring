from django.urls import path, include

from monitoring.mixin import get_main_memory_swap_memory
from monitoring.views import DashboardView

monitoring_patterns = (
    [
        path('memory/', get_main_memory_swap_memory, name='main-memory-swap-memory'),
    ],
    'monitoring'
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('get-monitoring-data/', include(monitoring_patterns)),
]
