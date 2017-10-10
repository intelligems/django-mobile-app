from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.utils.uuid import get_fresh_uuid


class MobileDeviceBase(models.Model):
    id = models.CharField(
        max_length=60,
        primary_key=True,
        unique=True,
        default=get_fresh_uuid
    )
    push_token = models.CharField(
        verbose_name=_('Device Push Token'),
        max_length=250, default='',
        help_text=_('APN or GCM Token')
    )
    arn_endpoint = models.CharField(
        verbose_name=_('Device ARN Endpoint'),
        max_length=250, default='',
        help_text=_('ARN endpoint provided by AWS')
    )

    class Meta:
        abstract = True


