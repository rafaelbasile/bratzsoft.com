
from django.contrib import admin
from django.conf import settings
from bratzsoft.sap.models import Host, LinkURL, Note, System, LandscapeRole, Category, Product, Component, Parameter, AbapUser
from bratzsoft.core.models.crmmodels import Customer


class HostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('hostname', 'customer','ipv4','active')
    search_fields = ['hostname','customer','ipv4']

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name',)
    search_fields = ['name',]


class LinkURLAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('link','category','active')
    search_fields = ['link','category',]
    list_filter = ('link', 'category',)

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('number', 'title', 'component','category','update_date','active')
    search_fields = ['number','title','category','component']
    list_filter = ('category', 'component','active')


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'version',)
    search_fields = ['name','version']


class SystemAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('sid', 'instance_number', 'customer','active')
    search_fields = ['sid','customer']
    list_filter = ('customer','sid', 'active')


class LandscapeRoleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name',)
    search_fields = ['name',]
    list_filter = ('active',)

class ComponentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name',)
    search_fields = ['name','description']
    list_filter = ('name','active')


class ParameterAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'value',)
    search_fields = ['name','value',]

class AbapUserAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('username','sid','client')
    search_fields = ['username','sid']
    list_filter = ('sid','active')





# Site Header Text
# TBT To be changed for a settings variable/settings table

admin.site.site_header = settings.ADMIN_SITE_HEADER



#Admin Registrations

admin.site.register(Host, HostAdmin)
admin.site.register(LinkURL, LinkURLAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(LandscapeRole, LandscapeRoleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(AbapUser, AbapUserAdmin)
