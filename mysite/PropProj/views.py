from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import json


def hello_world(request):
    #parts = Part.objects.all()
    parts = Part.objects.all()
    part_types = set(map(lambda x:x.Type, parts[:]))
    catalog = []
    for part_type in part_types:
        current_parts = list(filter(lambda x: x.Type == part_type, parts))

        category_items = []
        for part in current_parts:
            current_specs = PartSpecs.objects.filter(PartID=part)

            ready_specs = []
            for spec in current_specs:
                name = spec.SpecID.Name
                value = spec.value
                ready_specs.append((name, value))

            category_items.append({
                "name": part.Name,
                "specs": ready_specs
            })
        catalog.append({
            "name": part_type,
            "items": category_items
        })
    print(catalog)


    return render(request, "configurator.html", {"catalog": json.dumps(catalog)})
    #if part.Type != part.Type + 1:

def index(request):
    return render(request,"index.html")
def help(request):
    return render(request,"help.html")

def login_user(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        username = request.POST.get('login')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return redirect('/register')
        else:
            login(request, user)
            return redirect('/PropProj')

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        user = User()
        user.username = request.POST.get('login')
        user.set_password(request.POST.get('password'))
        user.save()

        login(request, user)

        return redirect('/PropProj')

def add_drone(request):
    return render(request,'drone_sn.html')