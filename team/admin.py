from django.contrib import admin
from .models import Team
# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    '''Admin View for Team'''
    
    list_display = ('name','title', 'created_at')
    list_filter = ('name',)
    readonly_fields = ('created_at','updated_at')
    search_fields = ('name','title')
    ordering = ('name',)
