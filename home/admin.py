from django.contrib import admin

# Register your models here.
from .models import *

class projectImageInline(admin.StackedInline):
    model = ProjectGallery
    extra = 1

@admin.register(ProjectGallery)
class ProjectGallery(admin.ModelAdmin):
    list_display = ['project']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    inlines = [
        projectImageInline
    ]
