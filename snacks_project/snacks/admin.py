from django.contrib import admin
from .models import Snack

@admin.register(Snack)

class adminApp(admin.ModelAdmin):
    pass