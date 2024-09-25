Домашнее задание по теме "QuerySet запросы в базу данных"

Cписок QuerySet запросов в порядке вызовов, которые я использовал для внесения изменений в БД.

from task1.models import Buyer

Buyer.objects.create(name='Alex', balance='1500', age='25')

Buyer.objects.create(name='Anna', balance='1200', age='22')

Buyer.objects.create(name='Tom', balance='1100', age='17')

Buyer.objects.create(name='Max', balance='1000', age='33')

from task1.models import Game

Game.objects.create(title='S.T.A.L.K.E.R.: Чистое Небо', cost='200', size='25', description='Шутер', age_limited='True')  

Game.objects.create(title='S.T.A.L.K.E.R.: Зов Припяти', cost='300', size='30', description='Шутер', age_limited='False')

Game.objects.create(title='S.T.A.L.K.E.R.2: Сердце Чернобыля', cost='400', size='40', description='Шутер', age_limited='True') 

f = Buyer.objects.get(age__lt=18)

f
<Buyer: Tom>

first_buyer, second_buyer, fourth_buyer = Buyer.objects.filter(age__gt=18)

Game.objects.get(id=1).buyer.set((1, 2, 3, 4))

Game.objects.get(id=2).buyer.set((1, 2, 4))

Game.objects.get(id=3).buyer.set((1,))
