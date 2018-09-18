from django.conf.urls import url, include
from django.contrib import admin
from .routers import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', include('Api.urls')),
    url('api/', include (router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
