from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView


def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news_home.html', {'news':news})


class NewsDetailView(DetailView):
    model = Artiles
    template_name = "details_view.html"
    context_object_name = "article"


def create_news(request):
    error = ''
    if request.method == "POST":
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'creator.html', data)