# forms.py
from django import forms
from .models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'release_date']

        labels = {
            'title': 'Название фильма',
#            'director': 'Режиссер',
            'release_date': 'Дата выхода',
#            'genre': 'Жанр',
            'description': 'Описание',
        }

        help_texts = {
            'title': 'Введите название фильма',
            'description': 'Введите краткое описание фильма',
            'release_date': 'Введите дату выхода фильма YYYY-MM-DD',
        }


class DateForm(forms.Form):
    date = forms.DateField(input_formats=['%Y-%m-%d'])
