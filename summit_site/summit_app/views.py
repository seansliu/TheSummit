from django.http import HttpResponse
from django.shortcuts import render

from summit_app.models import Content


def index(request):
    latest_content_list = Content.objects.order_by('-pub_date')[:5]
    context = {'latest_content_list': latest_content_list}
    return render(request, 'summit_app/index.html', context)


def detail(request, content_id):
    return HttpResponse("This is the content id:\n%s" % content_id)


def results(request, content_id):
    return HttpResponse("This is the text of the content \n%s" % content_id)


def rate(request, content_id):
    return HttpResponse("You're rating on content \n%s" % content_id)
