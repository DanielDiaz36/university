# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from core.models import Student
from django.views import View
from django.contrib import messages
from core.forms.student import StudentForm
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utils.permissions import PermissionRequiredMixin
from django.utils.translation import gettext_lazy as _


class StudentListView(PermissionRequiredMixin, ListView):
    model = Student
    template_name = 'student/list.html'
    paginate_by = 10
    permission_required = ['admin']

    def get_queryset(self):
        object_list = Student.objects.all().order_by('name')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            object_list = object_list.filter(name__icontains=q)

        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_student'] = True
        return context


class StudentAddView(PermissionRequiredMixin, CreateView):
    model = Student
    template_name = "student/form.html"
    form_class = StudentForm
    success_url = reverse_lazy('students')
    permission_required = ['admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('add').capitalize()
        context['active_student'] = True
        return context

    def form_valid(self, form):
        student = form.save(commit=False)
        student.created_by_id = self.request.user.id
        student.updated_by_id = self.request.user.id
        student.save()
        messages.add_message(self.request, messages.SUCCESS, _("Successfully registered."))
        return super().form_valid(form)


class StudentDetailsAjaxView(TemplateView):

    def get(self, request, *args, **kwargs):

        student_id = request.GET['student_id']
        student = Student.objects.get(id=student_id)
        data = {
            'name': student.name,
            'age': student.age,
            'gender': student.gender.capitalize(),
            'email': student.email,
            'date_birthday': str(student.date_birthday.strftime("%d-%m-%Y")),
            'city_birthday': str(student.city_birthday.strftime("%d-%m-%Y")),
            'group': student.group.name,
            'is_active': str(student.is_active_()),
            'created_by': str(student.created_by.fullname()),
            'created_at': str(student.created_at.strftime("%d-%m-%Y")),
            'updated_by': str(student.updated_by.fullname()),
            'updated_at': str(student.updated_at.strftime("%d-%m-%Y")),
        }
        return HttpResponse(json.dumps(data), content_type='application/json')


class StudentEditView(PermissionRequiredMixin, UpdateView):
    model = Student
    template_name = "student/form.html"
    form_class = StudentForm
    success_url = reverse_lazy('students')
    permission_required = ['admin']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('edit').capitalize()
        context['active_student'] = True
        return context

    def form_valid(self, form):
        group = form.save(commit=False)
        group.updated_by_id = self.request.user.id
        group.save()
        messages.add_message(self.request, messages.SUCCESS, _("Successfully edited."))
        return super().form_valid(form)


class StudentDeleteView(PermissionRequiredMixin, View):
    permission_required = ['admin']

    def get(self, request, *args, **kwargs):
        try:
            obj = Student.objects.get(id=self.kwargs['pk'])
            obj.delete()
            messages.add_message(request, messages.SUCCESS, _("Successfully deleted."))
        except:
            messages.add_message(request, messages.ERROR, _("Error."))
        return JsonResponse({})


class StudentEnableView(PermissionRequiredMixin, View):
    permission_required = ['admin']

    def get(self, request, *args, **kwargs):
        try:
            obj = Student.objects.get(id=self.kwargs['pk'])
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, _("Successfully enabled."))
        except:
            messages.add_message(request, messages.ERROR, _("Error."))
        return JsonResponse({})


class StudentDisableView(PermissionRequiredMixin, View):
    permission_required = ['admin']

    def get(self, request, *args, **kwargs):
        try:
            obj = Student.objects.get(id=self.kwargs['pk'])
            obj.is_active = False
            obj.save()
            messages.add_message(request, messages.SUCCESS, _("Successfully disabled."))
        except:
            messages.add_message(request, messages.ERROR, _("Error."))
        return JsonResponse({})
