from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def test2(request):
    return HttpResponse("HOW ARE U")


def test3(request):
    return HttpResponse("Who")




