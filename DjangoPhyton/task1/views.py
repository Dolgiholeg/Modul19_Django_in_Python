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
        buyer_user = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        buyer = username in buyers
        if age is None:
            # Обработайте ситуацию, например, верните сообщение об ошибке или установите значение по умолчанию
            return render(request, 'registration_page.html', {'error': 'Age is required'})
        if password == repeat_password:
            if int(age) >= 18:
                if buyer == False:
                    buyer_user = True
                    # Buyer.objects.create(name=username, balance=0, age=age)
                    # print(f'Приветствуем {username}')
                    # return HttpResponse(f'Приветствуем {username}')
                else:
                    info['error'] = 'Пользователь уже существует'
                    # print(f'Пользователь уже существует')
                    # return HttpResponse('Пользователь уже существует')
            else:
                info['error'] = 'Вы должны быть старше 18 лет'
                # print(f'Вы должны быть старше 18 лет')
                # return HttpResponse(f'Вы должны быть старше 18 лет')
        else:
            info['error'] = 'Пароли не совпадают'
            # print(f'Пароли не совпадают')
            # return HttpResponse('Пароли не совпадают')

        if buyer_user:
            message = (f'Приветствуем, {username}!')
            Buyer.objects.create(name=username, balance=0, age=age)
                # print(message)
                # users2 = Buyer.objects.all().values()
                # print('Это покупатели', users2)
        else:
            message = info['error']
        return HttpResponse(message)
    return render(request, 'registration_page.html', info)
    # context = {'info': info, }
    # return render(request, 'registration_page.html', context)

# def sign_up_by_html(request):
#     buyers=[]
#     Buyers = Buyer.objects.all().values()
#     num = len(Buyers)
#     for i in range(num):
#         buyers.append(Buyers[i]['name'])
#     info = {}
#
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         username = form.request.POST.get('username')
#         password = form.request.POST.get('password')
#         repeat_password = form.request.POST.get('repeat_password')
#         age = form.request.POST.get('age')
#         buyer = username in buyers
#                 if age is None:
#             # Обработайте ситуацию, например, верните сообщение об ошибке или установите значение по умолчанию
#             return render(request, 'registration_page.html', {'error': 'Age is required'})
#         if buyer not in buyers and password == repeat_password and int(age) >= 18:
#             Buyer.objects.create(name=username, balance='0', age=age)
#             print(f'Приветствуем {username}')
#             return HttpResponse(f'Приветствуем {username}')
#
#         elif buyer in buyers:
#             info['error'] = HttpResponse('Пользователь уже существует')
#             print(f'Пользователь уже существует')
#             return HttpResponse('Пользователь уже существует')
#         elif password != repeat_password:
#             info['error'] = HttpResponse('Пароли не совпадают')
#             print(f'Пароли не совпадают')
#             return HttpResponse('Пароли не совпадают')
#         elif int(age) < 18:
#             info['error'] = HttpResponse(f'Вы должны быть старше 18 лет')
#             print(f'Вы должны быть старше 18 лет')
#             return HttpResponse(f'Вы должны быть старше 18 лет')
#
#     context = {'info':info}
#     return render(request, 'registration_page.html', context)
