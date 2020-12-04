from django.shortcuts import render
import datetime
from app1.models import Students, Classes, Grade, Lessons, OneLesson


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
    return render(request, 'app1/grade.html', {'name': name, 'grade': grade, 'url_name': url_name})


def frog(request):
    url_name = request.resolver_match.url_name
    date = datetime.datetime.now()
    return render(request, 'app1/main.html', {'date': date, 'url_name': url_name})


def authorization(request):
    print(request.method)
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = Students.objects.get(login=login, password=password)
        if len(user) == 1:
            if len(LogUser.objects.filter(user.id)) > 0:
                return HttpResponse(status=400)
            else:
                key = LogUser(key=user)
                key.save()
                return render(request, 'app1/main.html',
                              {'name': user.name, 'class': user.user_class, 'url_name': 'main'})
        else:
            return HttpResponse('Неправильное имя пользователя или пароль')
    else:
        return render(request, 'app1/form.html')
