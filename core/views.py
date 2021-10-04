from django.views.generic import TemplateView


class DashboardIndexView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Portal Inicio'
        context['page_info'] = 'Inicio'
        return context

