from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'discrimination/index.html')


def result(request):
    return render(request, 'discrimination/result.html')
