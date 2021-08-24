from enum import Enum
from django.utils.translation import gettext_lazy as _


class GenderEnum(Enum):

    FEMALE = 'female'

    MALE = 'male'

    CHOICES = (
        ('female', _('female')),

        ('male', _('male')),
    )
