Домашнее задание по теме "QuerySet запросы в базу данных"

Cписок QuerySet запросов в порядке вызовов, которые я использовал для внесения изменений в БД.

Windows PowerShell
(C) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

Установите последнюю версию PowerShell для новых функций и улучшения! https://aka.ms/PSWindows

PS C:\Python proekt\UrbanProekt\Modul19_Django_in_Python> cd DjangoPhyton

PS C:\Python proekt\UrbanProekt\Modul19_Django_in_Python\DjangoPhyton> python manage.py shell

Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32

Type "help", "copyright", "credits" or "license" for more information.(InteractiveConsole)

>>> from task1.models import Buyer
>>> 
>>> Buyer.objects.create(name='Oleg', balance='2000',age=52)
<Buyer: Oleg>
>>> 
>>> Buyer.objects.create(name='Elena', balance='2550',age=41) 
<Buyer: Elena>
>>> 
>>> Buyer.objects.create(name='Jon', balance='1112.2',age=39)  
<Buyer: Jon>
>>> 
>>> from task1.models import Game
>>> 
>>> bob = Game.objects.get(id=1)
>>> 
>>> bob.title = "DOOM"
>>> 
>>> bob.save()
>>> 
>>> bob.description = 'УЖАСЫ'
>>> 
>>> bob.save()
>>> 
>>> all_buyer = Buyer.objects.all()
>>> Buyer.objects.all()
>>>  
<QuerySet [<Buyer: Alex>, <Buyer: Anna>, <Buyer: Tom>, <Buyer: Max>, <Buyer: User>, <Buyer: Vlad>, <Buyer: Vlad>, <Buyer: Vlad>, <Buyer: Vlad>, <Buyer: Vlad>, <Buyer: Oleg>, <Buyer: Elena>, <Buyer: Jon>]>

>>> person = Buyer.objects.get(id=6)
>>> person.delete()
(1, {'task1.Buyer': 1})
>>> 
>>> person = Buyer.objects.get(id=7) 
>>> person.delete()
(1, {'task1.Buyer': 1})
>>> 
>>> person = Buyer.objects.get(id=8)  
>>> person.delete()
(1, {'task1.Buyer': 1})
>>> 
>>> person = Buyer.objects.get(id=9) 
>>> person.delete()
(1, {'task1.Buyer': 1})
>>> 
>>> Buyer.objects.filter(age=22)              
<QuerySet [<Buyer: Anna>, <Buyer: User>]>
>>>

