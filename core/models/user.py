# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models.user_category import UserCategory
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    date_joined = None

    first_name = models.CharField(max_length=100, blank=False, null=False)

    last_name = models.CharField(max_length=200, blank=False, null=False)

    email = models.EmailField(blank=False, null=False)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    # Extras:

    user_category = models.ForeignKey(UserCategory, on_delete=models.PROTECT)

    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)

    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    password_update_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.first_name

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        app_label = 'core'
        db_table = 'auth_user'
        ordering = ['username']
