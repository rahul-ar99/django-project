from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):

    context = { }
    return render(request, 'web/index.html',context=context)
