from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractMobileDevice(models.Model):
    """
    Abstract model to extend while creating your custom Devices model for your
    project. By default, this offers the bare-minimum fields to register push-enabled devices,
    register them on AWS SNS and store this information in the database.
    """

    APN = 'apn'
    GCM = 'gcm'
    DEVICE_TYPES = (
        (APN, 'APN'),
        (GCM, 'GCM')
    )

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4
    )
    push_device_type = models.CharField(
        verbose_name='Push Device Type',
        max_length=5, choices=DEVICE_TYPES,
        default=APN, help_text=_('APN or GCM')
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

    @property
    def is_ios(self):
        return True if self.push_device_type == self.APN else False

    @property
    def is_android(self):
        return True if self.push_device_type == self.GCM else False
