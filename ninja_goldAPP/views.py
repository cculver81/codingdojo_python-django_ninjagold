from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Go ninja, go ninja, go')

