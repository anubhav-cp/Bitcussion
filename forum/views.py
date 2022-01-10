from django.http.response import HttpResponse
from django.shortcuts import render



def homePage(request):
    return HttpResponse("hello world")