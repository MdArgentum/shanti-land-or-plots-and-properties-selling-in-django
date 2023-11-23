from django.contrib import admin
from .models import Land
# Register your models here.

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    '''Admin View for Land'''

    list_display = ('name','is_featured','is_published','is_slider')
    prepopulated_fields = {'name_slug': ('name',)}
    list_filter = ('name',)
    list_editable =('is_featured','is_published','is_slider')

    readonly_fields = ('created_at',)
    search_fields = ('name',)
    ordering = ('name',)