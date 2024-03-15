from django.shortcuts import render


def index(request):
    return render(request, 'poll/pages/index.html')
