from django.shortcuts import render
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
    return request.GET