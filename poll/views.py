from django.http import HttpResponse
from django.shortcuts import render

from poll.models import Party


def index(request):
    poll = Party.objects.order_by('-votes')

    context = {
        'poll': poll,
        'page_title': ' | INDEX',
    }

    return render(request, 'poll/pages/index.html', context)


def register(request):
    return HttpResponse('REGISTER')


def login(request):
    return HttpResponse('LOGIN')


def logout(request):
    return HttpResponse('LOGOUT')


def vote(request):
    return HttpResponse('VOTE')


def update(request):
    return HttpResponse('UPDATE')
