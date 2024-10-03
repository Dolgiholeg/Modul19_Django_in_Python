from django.db import models

class Dogs(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название породы')
    foto = models.ImageField(upload_to='img/', verbose_name='Картинка')
    description = models.TextField(verbose_name='Описание породы')

    def __str__(self):
        return self.name
