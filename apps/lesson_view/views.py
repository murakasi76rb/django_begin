from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from apps.lesson_view.models import Menu

def main(request: HttpRequest) -> HttpResponse:
    return render(request, 'lesson_view/lesson1.html' , {'name': 'Ruslan'})



class FirstClass(View):
    def get(self, request: HttpRequest):
        context = {
            'numbers': [n for n in range(1,20)],
            'name': 'Admin',
        }
        return render(request, 'lesson_view/class_view.html', context)


class ProdustList(ListView):
    model = Menu
    template_name = 'lesson_view/list.html'
    context_object_name = 'menu'


