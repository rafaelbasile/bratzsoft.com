from django.contrib import admin
from .models import Loan, RendaFixa, InvestmentFund
# Register your models here.


class LoanAdmin(admin.ModelAdmin):
#	readonly_fields = ('created_at', 'updated_at')
    list_display = ('loan_name', 'person', 'date', 'value')
    search_fields = 'loan_name', 'person')


class RendaFixaAdmin(admin.ModelAdmin):
    #readonly_fields = ('created_at', 'updated_at')
#    list_display = ('name', 'symbol', 'sector', 'subSector', 'activity', 'market_segment')
#    search_fields = ['symbol', 'name']


class InvestmentFundAdmin(admin.ModelAdmin):
#   readonly_fields = ('created_at', 'updated_at')
   list_display = ('product_type', 'signer', 'start_date', 'tax', 'validity_date', 'position')
#   search_fields = ['stock', ]

admin.site.register(Loan, LoanAdmin)
admin.site.register(RendaFixa, RendaFixaAdmin)
admin.site.register(InvestmentFund, InvestmentFundAdmin)