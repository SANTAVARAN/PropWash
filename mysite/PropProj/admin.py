from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Part)
admin.site.register(Specs)
admin.site.register(PartSpecs)