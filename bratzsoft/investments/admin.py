from django.contrib import admin
from .models import Loan, Stock, StockQuote
# Register your models here.


from django.contrib import admin


class LoanAdmin(admin.ModelAdmin):
    #readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'date', 'value')
    search_fields = ['name', 'description']


class StockAdmin(admin.ModelAdmin):
    #readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'symbol', 'sector', 'subSector', 'activity', 'market_segment')
    search_fields = ['symbol', 'name']


class StockQuoteAdmin(admin.ModelAdmin):
    #readonly_fields = ('created_at', 'updated_at')
    list_display = ('stock', 'date', 'value')
    search_fields = ['stock', ]

admin.site.register(Loan, LoanAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(StockQuote, StockQuoteAdmin)