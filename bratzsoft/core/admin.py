from django.contrib import admin
from django.conf import settings
from .models import Host, LinkURL, Note, Customer, System, LandscapeRole, Category, Product, Component



class HostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('hostname', 'ipv4','customer','active')
    search_fields = ['hostname','ipv4','customer']

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
    list_display = ('number', 'title', 'category','component','active')
    search_fields = ['number','title','category','component']
    list_filter = ('category', 'component','active')


class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'email', 'description','active')
    search_fields = ['name','email']

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

# Site Header Text
# TBT To be changed for a settings variable/settings table

admin.site.site_header = settings.ADMIN_SITE_HEADER



#Admin Registrations

admin.site.register(Host, HostAdmin)
admin.site.register(LinkURL, LinkURLAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(LandscapeRole, LandscapeRoleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Component, ComponentAdmin)
