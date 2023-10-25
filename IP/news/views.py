from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm

def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news_home.html', {'news':news})

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