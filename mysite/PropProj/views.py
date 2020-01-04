from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return render(request, "index.html")
    #return HttpResponse("e8c65c56-6bde-4568-9017-b2f848990f98.JPG")
def index(request):
    return HttpResponse("Да")