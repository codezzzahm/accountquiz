from django.shortcuts import render
from .models import questions

def quiz(request):
    """Placeholder index view""" 
    quizquestion=questions.objects.all()
    return render(request, 'quiz.html', {'qiz':quizquestion })  