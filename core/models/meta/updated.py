from django.db import models
from django.utils.translation import gettext_lazy as _


class Updated(models.Model):
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
    updated_by = models.ForeignKey(
        'User', related_name='%(class)s_updated_by', on_delete=models.DO_NOTHING, verbose_name=_('updated by')
    )

    class Meta:
        abstract = True
