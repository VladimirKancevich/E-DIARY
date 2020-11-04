from django.shortcuts import render

from app1.models import Students, Classes


def main(request):
    return render(request, 'app1/main.html', )


def form(request):
    return render(request, 'app1/form.html', )


def student(request):
    name = Students.objects.all()
    return render(request, 'app1/grade.html', {'name': name})
