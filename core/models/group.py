# -*- coding: utf-8 -*-
from django.db import models
from core.models import Created, Updated, Deleted
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from core.models.professor_guide import ProfessorGuide


class Group(Created, Updated, Deleted):
    """
    Model to describe a group
    """

    name = models.CharField(verbose_name=_('name'), max_length=255)

    professor_guide = models.ForeignKey(ProfessorGuide, verbose_name=_('professor guide'), on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_group'
        verbose_name = _('group')
        verbose_name_plural = _('groups')
        ordering = ('is_deleted', 'created_at')
        default_permissions = []

    def delete(self, deleted_by=None, **kwargs):
        self.is_deleted = True
        self.deleted_by = deleted_by
        self.deleted_at = now()
        self.save()
