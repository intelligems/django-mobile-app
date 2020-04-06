# Django Mobile App <a href="https://www.intelligems.eu" target="_blank"><img src="https://intelligems.s3.amazonaws.com/intelligems_logo.png" width="40" height="40"></a>

An easy to use project template in Django 1.11, focused on a custom backend for a mobile app. [![Build Status](https://travis-ci.org/intelligems/django-mobile-app.svg?branch=master)](https://travis-ci.org/intelligems/django-mobile-app)

# Repository unmaintained
As Intelligems has stopped operations since Aug19, this repository remains unmaintained. Whoever may be interested to keep it up-to-date or extend it, DM [koslib](https://twitter.com/koslib) to arrange project transfer.

# General
This repo acts as a decent starting point for those who are looking for a custom backend deployment for their mobile app.
It includes a full-serving django project which exposes a RESTful API, manages user instances and is highly configurable.

In fact, this project is not a package that you can include in your project and use right-away, but it's a project template that you can download, 
extend and keep working on it as a base for your new project.

3rd-party apps it includes:
- `django-storages`, to store files in AWS S3 (the most commonly used object storage)
- `django-allauth`, for social media authentication
- `django-anymail[mailgun]`, to send transactional emails using Mailgun (first 10k messages/month are free)
- `djangorestframework`, for the RESTful API
- `django-rest-swagger`, to automatically generate documentation for your RESTful API endpoints
- `django-rest-auth`, to provide social media authentication over the API
- `django-filters`, which provides filtering capabilities in the DRF API views
- `django-guardian`, for custom object or model level permissions
- `celery`, for background tasks handling. By default, it's expected to be used for device registration on the AWS SNS service.
- `django-extensions`, offering a collection of custom extensions for Django
- `django-environ`, following the 12-factor methodology
 
# Prerequisites
- Python3
- Git
- pip
- virtualenv (recommended)

# How to use
1. Clone this repo on your local machine: 
```bash
git clone https://github.com/intelligems/django-mobile-app
```
2. We strongly advise to create a Python virtual environment and install the project requirements in there: 
```bash
mkvirtualenv <env-name> --python=`which python3`
``` 
3. Install project requirements inside your newly created local virtual environment:
```bash
pip install -r requirements.txt
```
4. Inside the `settings` path, create an `.env` file. Add in there all the environment variables that should be included
in the project runtime.
5. It's time to perform your first database migrations - no worries, we have included them too:
```bash
python manage.py migrate
```
6. Run the server!
```bash
python manage.py runserver 0.0.0.0:80
```

# Registering Push Devices
For the `push_devices` app usage, you are expected to use the `AbstractMobileDevice` abstract model.
You can extend it and add any fields you wish, but you are not allowed (by Django) to override the same fields that the `AbstractMobileDevice` model uses.

In order to create a push device, inside the create view of your devices' API, import the sns registration method
```python
from core.mobile_devices.tasks import register_device_on_sns
```
and use the `delay` method to register the newly created device on SNS. This will assign the ARN endpoint on the device model, so that you will be able to publish push notifications to your registered push device.

For example: 
```python
device = Device.objects.create(**data)
register_device_on_sns.delay(device)
```
