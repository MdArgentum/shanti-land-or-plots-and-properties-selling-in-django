from django.contrib import admin
from .models import About
# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    '''Admin View for About'''

    list_display = ('name',)
    def has_add_permission(self, request):
        # Deny permission to add new items
        return False