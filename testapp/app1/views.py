from django.shortcuts import render
import datetime
from app1.models import Students, Classes, Grade, Lessons, OneLesson


def main(request):
    return render(request, 'app1/main.html', )


def form(request):
    return render(request, 'app1/form.html', )


def student(request):
    name = Lessons.objects.all()
    grade = Grade.objects.all()
    return render(request, 'app1/grade.html', {'name': name, 'grade': grade})


def frog(request):
    date = datetime.datetime.now()
    return render(request, 'app1/main.html', {'date': date})
