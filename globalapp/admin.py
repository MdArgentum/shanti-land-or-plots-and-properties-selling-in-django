from django.contrib import admin
from .models import GlobalAuth
# Register your models here.

@admin.register(GlobalAuth)
class GlobalAuthAdmin(admin.ModelAdmin):
    '''Admin View for GlobalAuth'''

    list_display = ('title',)
    def has_add_permission(self, request):
        # Deny permission to add new items
        return False