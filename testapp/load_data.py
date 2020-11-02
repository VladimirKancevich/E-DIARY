from app1.models import Classes, Students, Teachers, Lessons, OneLesson, Grade

import json

with open('data.json', 'r') as file:
    data = json.load(file)

for cls in data['classes']:
    classes = Classes(name=cls['name'])
    classes.save()

for std in data['students']:
    student = Students(login=std['login'], password=std['password'], user_class=std['user_class'], name=std['name'])
    student.save()

for tch in data['teachers']:
    teacher = Teachers(login=tch['login'], password=tch['password'], name=tch['name'])
    teacher.save()

for les in data['lessons']:
    lesson = Lessons(name=les['name'], is_active=les['is_active b'])
    lesson.save()

for oles in data['one_lesson']:
    teacher = OneLesson(date_time=oles['date_time'], lesson=oles['lesson'], homework=oles['homework'], teacher=oles['teacher'], a_class=oles['a_class'], lesson_status=oles['lesson_status'])
    teacher.save()

for ex_c in data['grade']:
    grade = Grade(name=ex_c['name'])
    grade.save()
