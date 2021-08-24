# -*- coding: utf-8 -*-
from django.db import models
from core.models import Created, Updated, Deleted
from django.utils.translation import ugettext_lazy as _


class ProfessorGuide(Created, Updated, Deleted):

    name = models.CharField(verbose_name=_('name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_professor_guide'
        verbose_name = _('Professor guide')
        verbose_name_plural = _('Professor guide')
        ordering = ['name']
