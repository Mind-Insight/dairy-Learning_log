from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Регистрирует нового пользователя."""

    form = UserCreationForm(data=request.POST or None)
    if form.is_valid():
        new_user = form.save()
        # Выполнение входа и перенаправление на домашнюю страницу
        login(request, new_user)
        return redirect("learning_logs:home")

    context = {"form": form}
    return render(request, "users/register.html", context)
