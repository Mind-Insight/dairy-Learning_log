from django.shortcuts import render
from .models import Topic


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
