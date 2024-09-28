from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from django.views.generic import TemplateView
from .models import *


def index(request):
    Buyers = Buyer.objects.all()
    context = {
        'Buyers': Buyers,
    }
    return render(request, 'index.html', context)

def главная_view(request):
    title = 'мой сайт начало'
    text = 'Главная страница'
    context = {'title': title, 'text': text}
    return render(request, 'Главная.html', context)

def магазин_view(request):
    title = 'мой сайт магазин'
    text = 'Магазин'
    gamesdict = Game.objects.all().values()
    text4 = 'ВЕРНУТЬСЯ НА ГЛАВНУЮ'
    context = {'title': title, 'text': text, 'gamesdict': gamesdict, 'text4': text4}
    return render(request, 'Магазин.html', context)

def корзина_view(request):
    title = 'мой сайт корзина'
    text = 'Корзина'
    text1 = 'Извините Ваша корзина пуста'
    text4 = 'ВЕРНУТЬСЯ НА ГЛАВНУЮ'
    context = {'title': title, 'text': text, 'text1': text1, 'text4': text4}
    return render(request, 'Корзина.html', context)

def sign_up_by_html(request):
    buyers = []
    Buyers = Buyer.objects.all().values()
    for i in range(len(Buyers)):
        buyers.append(Buyers[i]['name'])
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        buyer = username in buyers
        if age is None:
            # Обработка ситуации, вернёт сообщение об ошибке
            return render(request, 'registration_page.html', {'error': 'Age is required'})
        if buyer == False and password == repeat_password and int(age) >= 18:
            Buyer.objects.create(name=username, balance=0, age=age)
            return HttpResponse(f'Приветствуем {username}')
        elif buyer == True:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse('Пользователь уже существует')
        elif password != repeat_password:
            info['error'] = 'Вы должны быть старше 18 лет'
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse(f'Вы должны быть старше 18 лет')
    context = {'info': info}
    return render(request, 'registration_page.html', context)


# def sign_up_by_django(request):
#     buyers=[]
#     Buyers = Buyer.objects.all().values()
#     num = len(Buyers)
#     for i in range(num):
#         buyers.append(Buyers[i]['name'])
#     info = {}
#
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         username = form.cleaned_data.POST.get('username')
#         password = form.cleaned_data.POST.get('password')
#         repeat_password = form.cleaned_data.POST.get('repeat_password')
#         age = form.cleaned_data.POST.get('age')
#         buyer = username in buyers
#         if age is None:
#             # Обработка ситуации, вернёт сообщение об ошибке
#             return render(request, 'registration_page.html', {'error': 'Age is required'})
#         if buyer == False and password == repeat_password and int(age) >= 18:
#             Buyer.objects.create(name=username, balance=0, age=age)
#             return HttpResponse(f'Приветствуем {username}')
#         elif buyer == True:
#             info['error'] = 'Пользователь уже существует'
#             return HttpResponse('Пользователь уже существует')
#         elif password != repeat_password:
#             info['error'] = 'Вы должны быть старше 18 лет'
#             return HttpResponse('Пароли не совпадают')
#         elif int(age) < 18:
#             info['error'] = 'Пароли не совпадают'
#             return HttpResponse(f'Вы должны быть старше 18 лет')
#     context = {'info': info}
#     return render(request, 'registration_page.html', context)