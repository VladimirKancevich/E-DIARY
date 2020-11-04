from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.main, name='main'),
    path('grade', views.student, name='grade'),
    path('form', views.form, name='form'),
]