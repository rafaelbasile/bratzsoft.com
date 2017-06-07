from django.contrib import admin
from django.conf import settings
from bratzsoft.sap.param.models import Parameter


class ParameterAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'value',)
    search_fields = ['name','value',]




admin.site.register(Parameter, ParameterAdmin)
