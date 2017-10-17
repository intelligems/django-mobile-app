import boto3
import logging
from django.conf import settings
from celery import shared_task


@shared_task
def register_device_on_sns(device):
    """
    Registers your device on AWS SNS and attaches the ARN endpoint on the device object.
    The ARN endpoint is used when publishing push notifications.
    :param device: your device object, extending the AbstractMobileDevice.
    :return: -
    """
    try:
        client = boto3.client('sns', region_name=settings.AWS_REGION)
        platform_arn = settings.AWS_IOS_APPLICATION_ARN if device.is_ios else settings.AWS_ANDROID_APPLICATION_ARN
        response = client.create_platform_endpoint(
            PlatformApplicationArn=platform_arn,
            Token=device.push_token,
        )
        endpoint_arn = response.get('EndpointArn')
        device.arn_endpoint = endpoint_arn
        device.save()
    except Exception as e:
        logging.error(e)
