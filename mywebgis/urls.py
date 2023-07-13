from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path("geoadmin/", admin.site.urls),
    path("api/v1/", include("onyeshamap.urls")),
]
