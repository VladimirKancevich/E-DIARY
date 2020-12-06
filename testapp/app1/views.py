from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
import datetime
from app1.models import *
from django.core.exceptions import ObjectDoesNotExist


def main(request):
    if len(LogUser.objects.all()) == 0:
        return redirect('/form')
    url_name = request.resolver_match.url_name
    user = LogUser.objects.all()[0].key
    user_name = user.name
    user_class = user.user_class
    return render(request, 'app1/main.html', {'url_name': url_name, 'class': user_class, 'name': user_name})


def homework(request):
    if len(LogUser.objects.all()) == 0:
        return redirect('/form')
    url_name = request.resolver_match.url_name
    user = LogUser.objects.all()[0].key
    user_name = user.name
    user_class = user.user_class
    return render(request, 'app1/homework.html', {'url_name': url_name, 'class': user_class, 'name': user_name})


def timetable(request):
    if len(LogUser.objects.all()) == 0:
        return redirect('/form')
    url_name = request.resolver_match.url_name
    user = LogUser.objects.all()[0].key
    user_name = user.name
    user_class = user.user_class
    return render(request, 'app1/timetable.html', {'url_name': url_name, 'class': user_class, 'name': user_name})


def progress_table(request):
    if len(LogUser.objects.all()) == 0:
        return redirect('/form')
    url_name = request.resolver_match.url_name
    user = LogUser.objects.all()[0].key
    user_name = user.name
    user_class = user.user_class
    return render(request, 'app1/progress_table.html', {'url_name': url_name, 'class': user_class, 'name': user_name})


def student(request):
    if len(LogUser.objects.all()) == 0:
        return redirect('/form')
    url_name = request.resolver_match.url_name
    name = Lessons.objects.all()
    grade = Grade.objects.all()
    user = LogUser.objects.all()[0].key
    user_name = user.name
    user_class = user.user_class
    return render(request, 'app1/grade.html', {'url_name': url_name, 'class': user_class, 'name': user_name})


def authorization(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        try:
            user = Students.objects.get(login=login, password=password)
            if len(LogUser.objects.filter(key=user)) > 0:
                key = LogUser.objects.all()[0]
                key.delete()
                key = LogUser(key=user)
                key.save()
                return redirect('/')
            else:
                key = LogUser(key=user)
                key.save()
                return redirect('/')
        except ObjectDoesNotExist:
            return HttpResponse(status=400)
    else:
        return render(request, 'app1/form.html')


def quit(request):
    user = LogUser.objects.all()[0]
    user.delete()
    return render(request, 'app1/form.html')
