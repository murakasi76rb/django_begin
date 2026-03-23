from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse
def main(request: HttpRequest) -> HttpResponse:
    return render(request, 'lesson_view/lesson1.html' , {'name': 'Ruslan'})
