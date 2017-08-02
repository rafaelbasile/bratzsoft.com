
from django.contrib import admin
from django.conf import settings
from bratzsoft.sap.models import Host, Note, SAPSystem, LandscapeRole, Category, Component, Parameter, AbapUser
from bratzsoft.accounts.models import Customer


class HostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('hostname', 'customer', 'active')
    search_fields = ['hostname', 'customer']

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', )
    search_fields = ('name', )


# class LinkURLAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_at','updated_at')
#     list_display = ('link','category','active')
#     search_fields = ['link','category',]
#     list_filter = ('link', 'category',)

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('number', 'version', 'title', 'component', 'category', 'relesed_on', 'active')
    search_fields = ('number', 'version', 'title', 'category', 'component')
    list_filter = ('category', 'component', 'active')


class SAPSystemAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('sid', 'instance_number', 'customer', 'active')
    search_fields = ('sid', 'customer')
    list_filter = ('customer', 'sid', 'active')


class LandscapeRoleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'active')
    search_fields = ('name', )
    list_filter = ('active',)

class ComponentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name',)
    search_fields = ('name', 'description')
    list_filter = ('name', 'active')


class ParameterAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'value', )
    search_fields = ('name', 'value', )

class AbapUserAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('username', 'sap_system', 'client')
    search_fields = ('username', 'sap_system')
    list_filter = ('sap_system', 'active')


# Site Header Text
# TBT To be changed for a settings variable/settings table

admin.site.site_header = settings.ADMIN_SITE_HEADER


#Admin Registrations

admin.site.register(Host, HostAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(SAPSystem, SAPSystemAdmin)
admin.site.register(LandscapeRole, LandscapeRoleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(AbapUser, AbapUserAdmin)
