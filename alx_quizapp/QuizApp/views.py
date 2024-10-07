from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        return HttpResponse("<h1>ERR 1 :: request != \'GET\' YABN ELKALB</h1>")
