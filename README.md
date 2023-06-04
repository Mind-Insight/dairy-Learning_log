# *Онлайн-ежедневник Learning-log*

Learning Log - это веб-приложение, при помощи которого
пользователь сможет вести журнал интересующих его тем и создавать записи
в журнале во время изучения каждой темы. Домашняя страница Learning Log
содержит описание сайта и приглашает пользователя зарегистрироваться
либо ввести свои учетные данные. После успешного входа пользователь получает возможность создавать новые темы, добавлять новые записи, читать
и редактировать существующие записи.

## Установка

Как установить и запустить проект

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Mind-Insight/dairy-Learning_log.git
```
2. Создайте виртуальное окружение с использованием `venv`:

```bash
cd social_network/
python3 -m venv venv
```

3. Активируйте виртуальное окружение:

```bash
source venv/bin/activate
```

4. Установите зависимости:

```bash
pip install -r requirements.txt
```

5. Запустите приложение:

```bash
python manage.py runserver
```

## Использование

Как использовать ваше приложение

1. Откройте браузер и перейдите по адресу `http://localhost:8000/`

2. Войдите в систему, используя свои учетные данные

3. Создайте первую запись в ежедневнике

## Функциональность

- Регистрация пользователей на сайте
- Создание запиисей, их изменение и удаление

## Технологии

Список технологий, используемых в проекте

* Python 3.11
* Django
* HTML
* CSS
* JavaScript
* Bootstrap

## Примеры кода

### views.py

```python
from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def new_topic(request):
    """Определяет новую тему"""
    if request.method != "POST":
        # Данные не отправились; создается пустая форма
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")

    # Вывести пустую или недействительную форму
    context = {"form": form}
    return render(request, "main/new_topic.html", context)


def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме."""

    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    context = {
        "topic": topic,
        "form": form,
    }
    return render(request, "main/new_entry.html", context)
```

### models.py

```python
from django.db import models


class Topic(models.Model):
    """Тема, которую изучает пользователь"""

    text = models.CharField(max_length=200)  # CharField - для хранения текста
    date_added = models.DateTimeField(
        auto_now_add=True
    )  # DateTimeField - для хранения даты и времени
    # auto_add_now=True - присваивание атрибуту текущую дату и
    # время при создании новой темы

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
        verbose_name_plural = "entries"

    def __str__(self):
        return f"{self.text[:50]}"
```

### forms.py
```python
from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        """
        Сообщает на какой модели должна базироавться форма
        и какие поля на ней должны находиться
        """

        model = Topic
        fields = ["text"]
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": "Entry"}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}

```

## Как внести свой вклад

1. Форкните репозиторий

2. Создайте свою ветку:

```bash
git checkout -b my-feature-branch
```

3. Внесите изменения и зафиксируйте их:

```bash
git commit -am 'Add some feature'
```

4. Загрузите изменения в свой форк:

```bash
git push origin my-feature-branch
```

5. Создайте pull request в оригинальный репозиторий

6. Ожидайте рассмотрения и подтверждения pull request
