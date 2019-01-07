from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'^', include('onyeshamap.urls')),
]
