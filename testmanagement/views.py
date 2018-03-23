from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def test(request):
    return HttpResponse("poda dei")


def test1(request):
    return HttpResponse("Hello")




