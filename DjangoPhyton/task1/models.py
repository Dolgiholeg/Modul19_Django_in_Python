from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя покупателя(username аккаунта)')
    balance = models.DecimalField(max_digits=4,decimal_places=2,verbose_name='Ваш баланс')
    age = models.IntegerField(verbose_name='Ваш возраст')

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100,verbose_name='Название игры')
    cost = models.DecimalField(max_digits=3,decimal_places=2, verbose_name='Цена')
    size = models.DecimalField(max_digits=3,decimal_places=2, verbose_name='Размер файлов игры')
    description = models.TextField(verbose_name='Описание игры')
    age_limited = models.BooleanField(default=False, verbose_name='Ограничение возраста 18+')
    buyer = models.ManyToManyField(Buyer, verbose_name='Обладатель книги')

    def __str__(self):
        return self.title
