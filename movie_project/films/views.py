# views.py

# Create your views here.
from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


def thank_you(request):
    return render(request, 'films/thank_you.html')


def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
        #            return redirect('films:film_list')
        return redirect('thank_you')  # Перенаправление на "Страницу спасибо"
    else:
        form = FilmForm()
    #    return render(request, 'films/film_list.html', {'form': form})
    return render(request, 'films/add_film.html', {'form': form})


def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})


class FilmListView(ListView):
    model = Film
    template_name = 'films/film_list.html'  # Убедитесь, что этот шаблон существует


class FilmCreateView(CreateView):
    model = Film
    fields = ['title', 'description', 'release_date']
    template_name = 'films/film_form.html'  # Убедитесь, что этот шаблон существует

    def get_success_url(self):
        return reverse_lazy('thank_you')
