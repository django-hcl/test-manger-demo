from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def test(request):
    return HttpResponse("hi")
