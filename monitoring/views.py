from django.views.generic import TemplateView

__author__ = 'Shafikur Rahman'


class DashboardView(TemplateView):
    template_name = 'monitoring/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['page_headline'] = 'Dashboard'
        return context
