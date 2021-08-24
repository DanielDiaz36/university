from django.db import models
from django.utils.translation import gettext_lazy as _


class Created(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    created_by = models.ForeignKey(
        'User', related_name='%(class)s_created_by', on_delete=models.DO_NOTHING, verbose_name=_('created by')
    )

    class Meta:
        abstract = True
