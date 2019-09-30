from django.urls import path, include

from monitoring.mixin import get_main_memory_swap_memory, get_network_information, get_uptime, get_traffic, \
    get_current_users
from monitoring.views import DashboardView

monitoring_patterns = (
    [
        path('memory/', get_main_memory_swap_memory, name='main-memory-swap-memory'),
        path('network/', get_network_information, name='network'),
        path('uptime/', get_uptime, name='uptime'),
        path('traffic/', get_traffic, name='traffic'),
        path('current-user/', get_current_users, name='current-user'),
    ],
    'monitoring'
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('get-monitoring-data/', include(monitoring_patterns)),
]
