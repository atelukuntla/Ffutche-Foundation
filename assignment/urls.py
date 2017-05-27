from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('ffutche.urls')),
    url(r'^admin/', admin.site.urls),
]
