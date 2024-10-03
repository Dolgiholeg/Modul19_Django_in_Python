from django.urls import path
from . import views


urlpatterns = [
    path('', views.главная_view, name='главная_view'),
    path('1/', views.магазин_view, name='магазин_view'),
    path('2/', views.корзина_view, name='корзина_view'),
    path('3/', views.sign_up_by_html, name='sign_up_by_html'),
    ]
