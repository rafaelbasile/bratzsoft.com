"""Investments Model."""
from django.db import models

class CompanySector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CompanySubSector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CompanySegment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ListingSegment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stock(models.Model):

    STOCK_TYPE_CHOICES = (
    ('ON', 'Ordinary'),
    ('PN', 'Preffered'),
        )

    symbol = models.CharField(max_length=8)
    stock_type = models.CharField(max_length=2, choices=STOCK_TYPE_CHOICES)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.symbol


class Company(models.Model):


    CATEGORY_CHOICES = (
    ('AL', 'Alerta'),
    ('NC', 'Não Classificada'),
    ('EQ', 'Equilibrada'),
        )


    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=4)
    stocks = models.ManyToManyField(Stock)
    cnpj = models.PositiveIntegerField()
    activity = models.CharField(max_length=100)
    sector = models.ForeignKey(CompanySector, on_delete=models.CASCADE)
    subsector = models.ForeignKey(CompanySubSector, on_delete=models.CASCADE)
    market_segment = models.ForeignKey(CompanySegment, on_delete=models.CASCADE)
    listing_segment = models.ForeignKey(ListingSegment, on_delete=models.CASCADE)
    market_value = models.CharField(max_length=100)
    ev = models.CharField(max_length=100)
    bookkeeper = models.CharField(max_length=100)
    majority_shareholder = models.CharField(max_length=100)
    site = models.URLField()
    headquarters= models.CharField(max_length=150)
    bovespa_page = models.URLField()
    shareholders = models.PositiveIntegerField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    ibov = models.BooleanField(default=False)
    next_balance = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"





class Loan(models.Model):
    loan_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    value = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=50)
    person = models.CharField(max_length=150)

    def __str__(self):
        return "%s - %s" % (self.person, self.loan_name)


class FixedIncome(models.Model):

    product_type = models.CharField(max_length=50)
    signer = models.CharField(max_length=100)
    start_date = models.DateField()
    due_date = models.DateField()
    validity_date = models.DateField()
    tax = models.CharField(max_length=50)
    available_amount = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=50)
    guarantee = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=50)
    start_amount = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=50)
    position = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=50)

    def __str__(self):
        return "%s - %s" % (self.product_type, self.signer)


class InvestmentFund(models.Model):
    FUND_TYPE_CHOICES = (
    ('RF', 'Renda Fixa'),
    ('MM', 'Multimercado'),
    ('FI', 'Fundo Imobiliário'),)

    ativo = models.CharField(max_length=100, unique=True)
    quota_date = models.DateField()
    quota_value = models.DecimalField(blank=True, null=True, decimal_places=8, max_digits=50)
    quote_amount = models.DecimalField(blank=True, null=True, decimal_places=8, max_digits=50)
    position = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=50)
    net_value = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=50)
    fund_type = models.CharField(max_length=2, choices=FUND_TYPE_CHOICES)
    
    def __str__(self):
        return self.ativo


class Broker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    OPERATION_TYPE = (
        ('BUY', 'Buy'),
        ('SEL', 'Sell'),
        ('DIV', 'Dividends'),
        ('SPL', 'Split'),
        ('AGR', 'Aggregation'),)

    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    operation_type = models.CharField(null=True,blank=True,max_length=3, choices=OPERATION_TYPE)
    operation_date = models.DateField()
    shares = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=9,max_digits=15)
    commission = models.DecimalField(decimal_places=2,max_digits=6)
    broker = models.ForeignKey(Broker)
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return '%s' % (str(self.stock.id))
