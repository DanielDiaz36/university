# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class City(models.Model):

    name = models.CharField(verbose_name=_('name'), max_length=255)

    is_active = models.BooleanField(verbose_name=_('is active'), default=True)

    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)

    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_city'
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        ordering = ['name']
