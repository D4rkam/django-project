from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin): #Con esta clase permite ver campos no modificables (solo lectura)
    readonly_fields = ('created', 'update')


admin.site.register(Project, ProjectAdmin)