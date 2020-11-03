from django.db import models


class Classes(models.Model):
    number = models.CharField(max_length=7)


class Users(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Students(Users):
    user_class = models.ForeignKey(Classes, on_delete=models.PROTECT)


class Teachers(Users):
    pass


class Lessons(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


class GradeType(models.IntegerChoices):
    lesson_work = 1
    test = 2
    control_test = 3
    homework = 4


class LessonStatus(models.IntegerChoices):
    active = 1
    canceled = 2
    switched = 3


class OneLesson(models.Model):
    date_time = models.DateTimeField()
    lesson = models.ForeignKey(Lessons, on_delete=models.PROTECT)
    homework = models.CharField(max_length=500, blank=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.PROTECT)
    a_class = models.ForeignKey(Classes, on_delete=models.PROTECT)
    lesson_status = models.IntegerField(choices=LessonStatus.choices)


class Grade(models.Model):
    student = models.ForeignKey(Students, on_delete=models.PROTECT)
    lesson = models.ForeignKey(OneLesson, on_delete=models.PROTECT)
    grade = models.IntegerField()
    grade_type = models.IntegerField(choices=GradeType.choices)

