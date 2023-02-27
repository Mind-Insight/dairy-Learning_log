from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # Главная старница
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),

    # Страница со списком тем
    path('topics/', views.show_topics, name='topics'),

    # Страница с подробной информацией по отедльной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
]
