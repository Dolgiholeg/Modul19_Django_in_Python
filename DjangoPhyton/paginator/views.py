from django.shortcuts import render
from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from django.shortcuts import render


def собаки_html(request):
    data = Dogs.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_data = paginator.get_page(page_number)
    return render(request, 'dogs.html', {'page_data': page_data})

def post_list(request):
    page_number = request.GET.get('page')
    try:
        page_data = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_data = paginator.page(1)
    except EmptyPage:
        page_data = paginator.page(paginator.num_pages)
    return render(request, 'dogs.html', {'page_data': page_data})


# # def post_list(request):
#     # получаем все посты
#     posts = Post.objects.all()
#
#     # создаем пагинатор
#     paginator = Paginator(posts, 10)  # 10 постов на странице
#
#     # получаем номер страницы, на которую переходит пользователь
#     page_number = request.GET.get('page')
#
#     # получаем посты для текущей страницы
#     page_posts = paginator.get_page(page_number)
#
#     # передаем контекст в шаблон
#     return render(request, 'post_list.html', {'page_posts': page_posts})

# def post_list(request):
#     # ...
#     page_number = request.GET.get('page')
#     try:
#         page_posts = paginator.get_page(page_number)
#     except PageNotAnInteger:
#         page_posts = paginator.page(1)
#     except EmptyPage:
#         page_posts = paginator.page(paginator.num_pages)
#
#     return render(request, 'post_list.html', {'page_posts': page_posts})

