from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm


def index(request):
    data = {
        'title': 'Main page',
    }
    return render(request, 'main/index.html', data)


def show_topics(request):
    """Выводит саисок тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'main/topics.html', context)


def topic(request, topic_id):
    """Выводит одну тему и все ее записи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'main/topic.html', context)


def about(request):
    return render(request, 'main/about.html')


def new_topic(request):
    """Определяет новую тему"""
    if request.method != 'POST':
        # Данные не отправились; создается пустая форма
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные
        form = Topic(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:topics')

    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'main/new_topic.html', context)