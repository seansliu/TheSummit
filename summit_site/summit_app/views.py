from django.http import HttpResponse
from django.shortcuts import render

from summit_app.models import Content


def index(request):
<<<<<<< HEAD
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'summit_app/index', context)
=======
    latest_content_list = Content.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_content_list}
    return render(request, 'summit_app/index.html', context)
>>>>>>> 21393d7e39249ad22588b92d41c959c37fcd0b44


def detail(request, question_id):
    return HttpResponse("This is the question id:\n%s" % question_id)


def results(request, question_id):
    return HttpResponse("This is the content of question \n%s" % question_id)


def rate(request, question_id):
    return HttpResponse("You're rating question \n%s" % question_id)
