from django.contrib import admin
from .models import Department


# FORCE UNREGISTER (this is the key fix)
try:
    admin.site.unregister(Department)
except admin.sites.NotRegistered:
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
