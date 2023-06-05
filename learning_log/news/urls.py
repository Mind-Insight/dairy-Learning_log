from django.urls import path
from . import views


app_name = "news"
urlpatterns = [
    path("", views.news_home, name="news_home"),
    path("create", views.create, name="create"),
    path("<int:pk>", views.NewsDetailView.as_view(), name="news_detail"),
    path(
        "<int:pk>/update", views.NewsUpdateView.as_view(), name="news_update"
    ),
    path(
        "<int:pk>/delete", views.NewsDeleteView.as_view(), name="news_delete"
    ),
]
