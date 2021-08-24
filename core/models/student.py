# -*- coding: utf-8 -*-
from django.db import models
from core.models import Created, Updated, Deleted
from core.utils.enums import GenderEnum
from core.models.group import Group
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class Student(Created, Updated, Deleted):
    """
    Model to describe a student
    """

    name = models.CharField(verbose_name=_('name'), max_length=255)

    age = models.IntegerField(verbose_name=_('age'))

    gender = models.CharField(verbose_name=_('gender'), max_length=10, choices=GenderEnum.CHOICES.value)

    email = models.EmailField(verbose_name=_('email'), unique=True)

    date_birthday = models.DateField(verbose_name=_('date of birthday'))

    city_birth = models.DateField(verbose_name=_('city of birthday'))

    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_student'
        verbose_name = _('student')
        verbose_name_plural = _('students')
        ordering = ('is_deleted', 'created_at')
        default_permissions = []

    def delete(self, deleted_by=None, **kwargs):
        self.is_deleted = True
        self.deleted_by = deleted_by
        self.deleted_at = now()
        self.save()
