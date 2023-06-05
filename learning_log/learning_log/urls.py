from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("learning_logs.urls")),
    path("users/", include("users.urls")),
    path("news/", include("news.urls")),
]
