# Django Mobile App

# General
This repo acts as a decent starting point for those who are looking for a custom backend deployment for their mobile app.
It includes a full-serving django project which exposes a RESTful API, manages user instances and is highly configurable.

3rd-party apps it includes:
- `django-storages`, to store files in AWS S3 (the most commonly used block storage)
- `django-allauth`, for social media authentication
- `django-anymail[mailgun]`, to send transactional emails using Mailgun (first 10k messages/month are free)
- `djangorestframework`, for the RESTful API
- `django-rest-swagger`, to automatically generate documentation for your RESTful API endpoints
- `django-rest-auth`, to provide social media authentication over the API
- `django-filters`, which provides filtering capabilities in the DRF API views
- `django-guardian`, for custom object or model level permissions
 