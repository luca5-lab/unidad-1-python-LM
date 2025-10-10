from django.contrib import admin
from dispositivos.models import Zona
from .models import Organization
#from accounts.models import UserProfile

class ZonaInline(admin.TabularInline):
    model = Zona
    extra = 0
    fields = ("nombre", "estado")
    show_change_link = True

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("name",)
    inlines = [ZonaInline]

