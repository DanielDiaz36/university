from django.db import models
from django.utils.translation import gettext_lazy as _


class Deleted(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name=_('deleted at'))
    deleted_by = models.ForeignKey(
        'User', related_name='%(class)s_deleted_by', on_delete=models.DO_NOTHING, null=True, blank=True,
        verbose_name=_('deleted by')
    )
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
