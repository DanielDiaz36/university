# -*- coding: utf-8 -*-
from django.urls import path
from .views.login import LoginView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import logout_then_login


urlpatterns = [

    path(_('login/'), LoginView.as_view(), name='login'),

    path(_('logout/'), logout_then_login, name='logout'),

]
