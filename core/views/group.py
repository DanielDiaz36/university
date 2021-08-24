# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from core.forms.group import GroupForm
from core.models import Group
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utils.permissions import PermissionRequiredMixin
from django.utils.translation import gettext_lazy as _


class GroupListView(PermissionRequiredMixin, ListView):
    model = Group
    template_name = 'group/list.html'
    paginate_by = 10
    permission_required = ['admin']

    def get_queryset(self):
        object_list = Group.objects.all().order_by('name')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            object_list = object_list.filter(name__icontains=q)

        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_group'] = True
        return context


class GroupAddView(PermissionRequiredMixin, CreateView):
    model = Group
    template_name = "group/form.html"
    form_class = GroupForm
    success_url = reverse_lazy('groups')
    permission_required = ['admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('add').capitalize()
        context['active_group'] = True
        return context

    def form_valid(self, form):
        group = form.save(commit=False)
        group.created_by_id = self.request.user.id
        group.updated_by_id = self.request.user.id
        group.save()
        messages.add_message(self.request, messages.SUCCESS, _("Successfully registered."))
        return super().form_valid(form)


class GroupDetailsAjaxView(TemplateView):

    def get(self, request, *args, **kwargs):

        group_id = request.GET['group_id']
        group = Group.objects.get(id=group_id)
        data = {
            'name': group.name,
            'professor_guide': group.professor_guide.name,
            'is_deleted': str(group.is_deleted_()),
            'created_by': str(group.created_by.fullname()),
            'created_at': str(group.created_at.strftime("%d-%m-%Y")),
            'updated_by': str(group.updated_by.fullname()),
            'updated_at': str(group.updated_at.strftime("%d-%m-%Y")),
        }
        return HttpResponse(json.dumps(data), content_type='application/json')


class GroupEditView(PermissionRequiredMixin, UpdateView):
    model = Group
    template_name = "group/form.html"
    form_class = GroupForm
    success_url = reverse_lazy('groups')
    permission_required = ['admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('edit').capitalize()
        context['active_group'] = True
        return context

    def form_valid(self, form):
        group = form.save(commit=False)
        group.updated_by_id = self.request.user.id
        group.save()
        messages.add_message(self.request, messages.SUCCESS, _("Successfully edited."))
        return super().form_valid(form)


class GroupDeleteView(PermissionRequiredMixin, View):
    permission_required = ['admin']

    def get(self, request, *args, **kwargs):
        try:
            obj = Group.objects.get(id=self.kwargs['pk'])
            obj.delete()
            messages.add_message(request, messages.SUCCESS, _("Successfully deleted."))
        except:
            messages.add_message(request, messages.ERROR, _("Error."))
        return JsonResponse({})


# class HabilitarProvinciaView(PermissionRequiredMixin, View):
#     permission_required = ['admin']
#
#     def get(self, request, *args, **kwargs):
#         provincia = Provincia.objects.get(id=self.kwargs['pk'])
#         provincia.activo = True
#         provincia.save()
#         messages.add_message(request, messages.SUCCESS, "Provincia habilitada con éxito.")
#         return JsonResponse({})
#
#
# class DeshabilitarProvinciaView(PermissionRequiredMixin, View):
#     permission_required = ['admin']
#
#     def get(self, request, *args, **kwargs):
#         provincia = Provincia.objects.get(id=self.kwargs['pk'])
#         provincia.activo = False
#         provincia.save()
#         messages.add_message(request, messages.SUCCESS, "Provincia deshabilitada con éxito.")
#         return JsonResponse({})
#
#
# class EliminarProvinciasSeleccionadasView(TemplateView):
#
#     def get(self, request, *args, **kwargs):
#
#         try:
#             ids = request.GET.get('ids').split(',')
#             Provincia.objects.filter(id__in=ids).delete()
#
#             mensaje = "Provincias eliminadas con éxito." if ids.__len__() > 1 else "Provincia eliminada con éxito."
#             messages.add_message(request, messages.SUCCESS, mensaje)
#
#         except:
#             messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")
#
#         return JsonResponse({})
