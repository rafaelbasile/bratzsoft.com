from django.contrib import admin
from .models.crmmodels import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'email', 'description','active')
    search_fields = ['name','email']


admin.site.register(Customer, CustomerAdmin)
