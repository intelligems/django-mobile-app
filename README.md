# Django Mobile App 
<a href="https://www.intelligems.eu" target="_blank"><img src="https://intelligems.s3.amazonaws.com/intelligems_logo.png" width="50" height="50"></a>

An easy to use project template in Django 1.11, focused on a custom backend for a mobile app. 

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
4. It's time to perform your first database migrations - no worries, we have included them too:
```bash
python manage.py migrate
```
5. Run the server!
```bash
python manage.py runserver 0.0.0.0:80
```