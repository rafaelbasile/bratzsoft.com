from django.contrib import admin
from .models import Loan, FixedIncome, InvestmentFund, Stock, Broker
# Register your models here.


class LoanAdmin(admin.ModelAdmin):
	list_display = ('date', 'loan_name', 'person', 'value')
	search_fields = ('loan_name', 'person')


class FixedIncomeAdmin(admin.ModelAdmin):
	list_display = ('product_type', 'signer', 'start_date', 'due_date', 'position')
	search_fields = ('product_type', 'signer')


class InvestmentFundAdmin(admin.ModelAdmin):
	list_display = ('ativo', 'fund_type', 'net_value')
	search_fields = ('ativo', 'fund_type',)


class StockAdmin(admin.ModelAdmin):
	list_display = ('symbol', 'quantity', 'price', 'operation_type', 'operation_date', 'broker',)
	search_fields = ('symbol',)
	list_filter = ('symbol','operation_type','broker',)


class BrokerAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)



admin.site.register(Broker, BrokerAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(FixedIncome, FixedIncomeAdmin)
admin.site.register(InvestmentFund, InvestmentFundAdmin)