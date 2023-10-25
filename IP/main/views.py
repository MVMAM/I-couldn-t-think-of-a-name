from django.shortcuts import render


def home(request):
    data = {
        'title':'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, "home.html", data)


def about(request):
    return render(request, "about.html")
