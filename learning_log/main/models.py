from django.db import models


class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)  # CharField - для хранения текста
    date_added = models.DateTimeField(auto_now_add=True)  # DateTimeField - для хранения даты и времени
    # auto_add_now=True - присваивание атрибуту текущую дату и время при создании новой темы

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    # ForeighKey - содержит ссылку на другую запись в базе данных
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    # отображение записей в порядке их создания
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}"
