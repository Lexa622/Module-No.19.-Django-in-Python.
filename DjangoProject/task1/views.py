from django.shortcuts import render
from .forms import UserRegister
from .models import *


def platform(request):
    title = "Главная страница"
    context = {"Title": title, }
    return render(request, 'platform.html', context)


def games(request):
    buy = "Купить"
    title = "Игры"
    games = Game.objects.all()
    context = {"games": games, "Title": title, "buy": buy, }
    return render(request, 'games.html', context)


def cart(request):
    title = "Корзина"
    text = "Извините, ваша корзина пуста"
    context = {"Title": title, "text": text, }
    return render(request, 'cart.html', context)


def sign_up_by_html(request):
    users = [i.name for i in Buyer.objects.all()]
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = int(request.POST.get("age"))
        if password == repeat_password and age >= 18 and username not in users:
            context = f"Приветствуем, {username}!"
            Buyer.objects.create(name=username, balance=0, age=age)
            return render(request, "registration_page.html", {"context": context})
        elif password != repeat_password:
            info['error'] = "Пароли не совпадают"
        elif age < 18:
            info['error'] = "Вы должны быть старше 18"
        elif username in users:
            info['error'] = "Пользователь уже существует"
    return render(request, "registration_page.html", context=info)


def sign_up_by_django(request):
    users = [i.name for i in Buyer.objects.all()]
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = int(form.cleaned_data["age"])
            if password == repeat_password and age >= 18 and username not in users:
                context = f"Приветствуем, {username}!"
                Buyer.objects.create(name=username, balance=0, age=age)
                return render(request, "registration_page.html", {"context": context})
            elif password != repeat_password:
                info['error'] = "Пароли не совпадают"
            elif age < 18:
                info['error'] = "Вы должны быть старше 18"
            elif username in users:
                info['error'] = "Пользователь уже существует"
        return render(request, "registration_page.html", context=info)
    else:
        form = UserRegister()
    return render(request, "registration_page.html", {"form": form})
