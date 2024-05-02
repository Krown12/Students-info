from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(students)
class taskadmin(admin.ModelAdmin):
    list_display=('name','description','is_selected')
    list_filter=('is_selected',)
    list_editable=('is_selected',)
    search_field =('name',)