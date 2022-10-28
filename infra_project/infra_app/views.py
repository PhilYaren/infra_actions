from django.http import HttpResponse


def index(request):
    return HttpResponse('Опупеть, вышло!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
