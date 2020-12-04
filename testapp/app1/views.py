from django.shortcuts import render
import datetime
from app1.models import Students, Classes, Grade, Lessons, OneLesson


def main(request):
    url_name = request.resolver_match.url_name
    return render(request, 'app1/main.html', {'url_name': url_name})


def form(request):
    url_name = request.resolver_match.url_name
    return render(request, 'app1/form.html', {'url_name': url_name})


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
    return render(request, 'app1/grade.html', {'name': name, 'grade': grade, 'url_name': url_name})


def frog(request):
    url_name = request.resolver_match.url_name
    date = datetime.datetime.now()
    return render(request, 'app1/main.html', {'date': date, 'url_name': url_name})
