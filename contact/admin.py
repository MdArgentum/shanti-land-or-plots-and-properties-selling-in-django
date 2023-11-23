from django.contrib import admin
from .models import Contact, Ltdinfo
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = ('name','subject')
    readonly_fields = ('created_at','updated_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

@admin.register(Ltdinfo)
class LtdinfoAdmin(admin.ModelAdmin):
    '''Admin View for Ltdinfo'''

    list_display = ('name','updated_at','is_active')
    list_editable = ('is_active',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    def has_add_permission(self, request):
        # Deny permission to add new items
        return False