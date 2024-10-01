from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.главная_view, name='главная_view'),
    path('1/', views.магазин_view, name='магазин_view'),
    path('2/', views.корзина_view, name='корзина_view'),
    path('3/', views.sign_up_by_html, name='sign_up_by_html'),
    path('dogs/', views.собаки_html, name='dogs_html'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)