# -*- coding: utf-8 -*-
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.contrib.auth.mixins import AccessMixin


class PermissionRequiredMixin(AccessMixin):
    """
    CBV Mixin: Verifica que el usuario actual posea los permisos especificados.
    """
    permission_required = None

    def get_permission_required(self):

        if self.permission_required is None:
            raise ImproperlyConfigured(
                '{0} is missing the permission_required attribute. Define {0}.permission_required, or override '
                '{0}.get_permission_required().'.format(self.__class__.__name__)
            )
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms

    def has_permission(self):
        perms = self.get_permission_required()
        user_category = self.request.user.user_category.category
        return perms.__contains__(user_category)

    def dispatch(self, request, *args, **kwargs):
        # Verifica primero que el usuario actual se encuentre autenticado.
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not self.has_permission():
            if settings.DEBUG:
                # DESARROLLO
                # Si el usuario no tiene permisos, se redirecciona a la página de inicio.
                return HttpResponseRedirect(reverse('home'))
            else:
                # PRODUCCION
                # Si el usuario no tiene permisos, se muestra la página de permiso denegado.
                raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


PERMS_HTML = {
    'admin': [
        'add-group',
        'edit-group',
        'delete-group',
        'add-student',
        'edit-student',
        'enable-student',
        'disable-student',
        'delete-student',
    ]
}
