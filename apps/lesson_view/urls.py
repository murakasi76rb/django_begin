from django.urls import path
from apps.lesson_view import views

app_name = 'lesson_view'

urlpatterns = [
path('', views.main, name='main'),
]
