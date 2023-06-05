from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


app_name = "news"
urlpatterns = [
    path("", views.news_home, name="news_home"),
    path("create", views.create, name="create"),
    path(
        "<int:pk>",
        login_required(views.NewsDetailView.as_view()),
        name="news_detail",
    ),
    path(
        "<int:pk>/update",
        login_required(views.NewsUpdateView.as_view()),
        name="news_update",
    ),
    path(
        "<int:pk>/delete",
        login_required(views.NewsDeleteView.as_view()),
        name="news_delete",
    ),
]
