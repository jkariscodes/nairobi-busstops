from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('geoadmin/', admin.site.urls),
    path('', include('onyeshamap.urls')),
]
