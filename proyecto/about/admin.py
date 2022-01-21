from django.contrib import admin
from .models import About

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
admin.site.register(About, AboutAdmin)