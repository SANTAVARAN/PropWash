from django.shortcuts import render
from django.http import HttpResponse
from .models import Part


def hello_world(request):
    #parts = Part.objects.all()
    parts = Part.objects.order_by('Type')
    SetParts=set(parts)
    Uparts=SetParts
    return render(request, "configurator.html", {"parts": parts})

    #if part.Type != part.Type + 1:


def index(request):
    return request.GET