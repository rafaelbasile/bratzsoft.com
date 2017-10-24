from django.contrib import admin
from .models import Loan, FixedIncome, InvestmentFund, Transaction, Broker, Company, CompanySegment, CompanySubSector, CompanySector, ListingSegment, Stock
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


class TransactionAdmin(admin.ModelAdmin):
	list_display = ('stock', 'shares', 'price', 'operation_type', 'operation_date', 'broker',)
	search_fields = ('stock',)
	list_filter = ('stock','operation_type','broker',)


class BrokerAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)


class CompanyAdmin(admin.ModelAdmin):
	list_display = ( 'symbol', 'name', 'sector','category','next_balance',)
	search_fields = ('name','symbol','category', )
	list_filter = ('symbol','sector','category',)

class CompanySectorAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

class CompanySubSectorAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

class CompanySegmentAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

class ListingSegmentAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)


class StockAdmin(admin.ModelAdmin):
	list_display = ('symbol', 'stock_type')
	search_fields = ('symbol',)




admin.site.register(Stock, StockAdmin)
admin.site.register(ListingSegment, ListingSegmentAdmin)
admin.site.register(CompanySector, CompanySectorAdmin)
admin.site.register(CompanySubSector, CompanySubSectorAdmin)
admin.site.register(CompanySegment, CompanySegmentAdmin)
admin.site.register(Broker, BrokerAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(FixedIncome, FixedIncomeAdmin)
admin.site.register(InvestmentFund, InvestmentFundAdmin)