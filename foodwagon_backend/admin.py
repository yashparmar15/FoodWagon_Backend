from django.contrib import admin

from foodwagon_backend.models import Venues,Trucks
from .models import Venues,Trucks

admin.site.register(Venues)
admin.site.register(Trucks)

