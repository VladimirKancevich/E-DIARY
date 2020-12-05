from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
import datetime
from app1.models import *
from django.core.exceptions import ObjectDoesNotExist


def main(request):
    url_name = request.resolver_match.url_name
    return render(request, 'app1/main.html', {'url_name': url_name})


def homework(request):
    url_name = request.resolver_match.url_name
    return render(request, 'app1/homework.html', {'url_name': url_name})


def timetable(request):
    url_name = request.resolver_match.url_name
    return render(request, 'app1/timetable.html', {'url_name': url_name})


def progress_table(request):
    url_name = request.resolver_match.url_name
    return render(request, 'app1/progress_table.html', {'url_name': url_name})


def student(request):
    url_name = request.resolver_match.url_name
    name = Lessons.objects.all()
    grade = Grade.objects.all()
    # user = Students.objects
    return render(request, 'app1/grade.html', {'name': name, 'grade': grade, 'url_name': url_name})


def frog(request):
    url_name = request.resolver_match.url_name
    date = datetime.datetime.now()
    return render(request, 'app1/main.html', {'date': date, 'url_name': url_name})


def authorization(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        try:
            user = Students.objects.get(login=login, password=password)
            if len(LogUser.objects.filter(key=user)) > 0:
                return redirect('')
            else:
                key = LogUser(key=user)
                key.save()
                return redirect('')
        except ObjectDoesNotExist:
            return HttpResponse(status=400)
    else:
        return render(request, 'app1/form.html')
