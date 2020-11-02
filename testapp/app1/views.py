from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello!!!")


def main(request):
    return render(request, 'app1/main.html',)


def form(request):
    return render(request, 'app1/form.html',)