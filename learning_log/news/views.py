from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def news_home(request):
    news = Articles.objects.order_by('title')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        # в form будут находится все данные, полученные от пользователя
        form = ArticlesForm(request.POST)
        # проверка на то, что являются ли данные корректными
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма!'

    form = ArticlesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
