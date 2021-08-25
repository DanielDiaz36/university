# -*- coding: utf-8 -*-
from django.db import models
from core.models import Created, Updated
from core.models.city import City
from core.utils.enums import GenderEnum
from core.models.group import Group
from django.utils.translation import gettext_lazy as _


class Student(Created, Updated):
    """
    Model to describe a student
    """

    name = models.CharField(verbose_name=_('name'), max_length=255)

    age = models.IntegerField(verbose_name=_('age'))

    gender = models.CharField(verbose_name=_('gender'), max_length=10, choices=GenderEnum.CHOICES.value)

    email = models.EmailField(verbose_name=_('email'), unique=True)

    date_birthday = models.DateField(verbose_name=_('date of birthday'))

    city_birthday = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name=_('city birthday'))

    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_student'
        verbose_name = _('student')
        verbose_name_plural = _('students')
        ordering = ('created_at',)
        default_permissions = []

    def is_active_(self):
        return _('Yes') if self.is_active else _('No')
