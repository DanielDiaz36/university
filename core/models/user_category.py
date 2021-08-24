# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserCategory(models.Model):

    category = models.CharField(verbose_name=_('name'), max_length=255)

    description = models.CharField(verbose_name=_('description'), max_length=255, null=True, blank=True)

    is_active = models.BooleanField(verbose_name=_('is active'), default=True)

    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)

    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    def __str__(self):
        return self.category

    class Meta:
        app_label = 'core'
        db_table = 'core_user_category'
        verbose_name = _('User category')
        verbose_name_plural = _('User categories')
        ordering = ['category']
