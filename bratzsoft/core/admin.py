from django.contrib import admin
from django.conf import settings
from .models import Host, LinkURL, Note, Customer, System



class HostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('hostname', 'ipv4','customer','active')
    search_fields = ['hostname','ipv4','customer']




class LinkURLAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('link','active')


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('number', 'title', 'category','component','active')
    search_fields = ['number','title','category','component']
    list_filter = ('category', 'component','active')


class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'email', 'description','active')
    search_fields = ['name','email']


class SystemAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('sid', 'instance_number', 'customer','active')
    search_fields = ['sid','customer']
    list_filter = ('customer','sid', 'active')


# Site Header Text
# TBT To be changed for a settings variable/settings table

admin.site.site_header = settings.ADMIN_SITE_HEADER



#Admin Registrations

admin.site.register(Host, HostAdmin)
admin.site.register(LinkURL, LinkURLAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(System, SystemAdmin)
