from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    data = {
        "title": "Main page",
    }
    return render(request, "main/index.html", data)


def show_topics(request):
    """Выводит саисок тем"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "main/topics.html", context)


def topic(request, topic_id):
    """Выводит одну тему и все ее записи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "main/topic.html", context)


def about(request):
    return render(request, "main/about.html")


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


def edit_entry(request, entry_id):
    """Редактирует существующую запись."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != "POST":
        # Исходный запрос; форма заполняется данными текущей записи.
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST; обработать данные.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=topic.id)

    context = {
        "entry": entry,
        "topic": topic,
        "form": form,
    }
    return render(request, "main/edit_entry.html", context)
