from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse
from .models import *


def index(request: HttpRequest) -> HttpResponse:
    quizzes = Quiz.objects.all()
    return render(request, 'index.html', context={"quizzes": quizzes})


def quiz_page(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    context = {"quiz": quiz, "questions": questions,
               "quiz_title": quiz.__str__()}
    return render(request, "quiz_page.html", context)
