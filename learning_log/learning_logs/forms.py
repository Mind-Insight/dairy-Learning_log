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
