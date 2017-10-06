from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from rest_framework_swagger.views import get_swagger_view

from users.api.auth_adapters import FacebookLogin, InstagramLogin

schema_view = get_swagger_view(title='Mobile App API')

router = SimpleRouter()
# register api routes using `router.register()`

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', schema_view),

    url(r'^api/v1/rest-auth/', include('rest_auth.urls')),
    url(r'^api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^api/v1/rest-auth/instagram/$', InstagramLogin.as_view(), name='instagram_login'),
    url(r'^api/v1/accounts/', include('users.api.urls')),
]
