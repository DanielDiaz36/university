# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from core.utils.permissions import PermissionRequiredMixin


class HomeView(PermissionRequiredMixin, TemplateView):
    template_name = 'pages/home.html'
    permission_required = ['admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_home'] = True
        return context
