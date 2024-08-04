# urls.py
from django.urls import path
from . import views

urlpatterns = [
    #    path('', views.film_list, name='film_list'),
    #    path('add/', views.add_film, name='add_film'),

    path('', views.FilmListView.as_view(), name='film_list'),  # Путь для главной страницы
    path('films/add/', views.add_film, name='add_film'), ## Добавлено для исправления ошибки
    path('add/', views.FilmCreateView.as_view(), name='film_add'),  # Вроде дублирует, но если убрать - ошибка
    path('thank_you/', views.thank_you, name='thank_you'),
]
