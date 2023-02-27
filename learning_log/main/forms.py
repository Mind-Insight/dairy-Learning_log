from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        """
        Сообщает на какой модели должна базироавться форма
        и какие поля на ней должны находиться
        """
        model = Topic
        fields = ['text']
        labels = {'text': ''}