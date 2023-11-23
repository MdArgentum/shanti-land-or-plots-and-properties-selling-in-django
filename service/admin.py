from django.contrib import admin
from .models import Service, Service_Video
# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    '''Admin View for Service'''
    list_display = ('service_id','name')
    ordering = ('service_id',)

@admin.register(Service_Video)
class Service_VideoAdmin(admin.ModelAdmin):
    '''Admin View for Service_Video'''

    list_display = ('description',)
    def has_add_permission(self, request):
        # Deny permission to add new items
        return False
