# -*- coding: utf-8 -*-
from django import template
from urllib import parse
from core.utils.permissions import PERMS_HTML

register = template.Library()


@register.filter
def is_delete_color(status):
    return 'disable' if status is True else 'enable'


@register.filter
def is_active_color(status):
    return 'enable' if status is True else 'disable'


@register.filter
def validate_perm(user_category, perm):
    return perm in PERMS_HTML.get(user_category)


@register.filter
def build_params(request_get, page):
    request_get = dict(request_get)
    request_get['page'] = [page]
    return f"?{parse.urlencode([(k, v[0]) for k, v in request_get.items() if v[0]])}"
