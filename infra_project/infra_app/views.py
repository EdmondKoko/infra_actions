from django.http import HttpResponse
from django.http.request import HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('У меня получилось!')


def second_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('А это вторая страница')
