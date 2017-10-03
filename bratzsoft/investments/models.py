"""Investments Model."""
from django.db import models


class Loan(models.Model):
    loan_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    value = models.DecimalField()
    person = models.CharField(max_length=150)

    def __str__(self):
        return "%s - %s" % (self.person, self.loan_name)


class FixedIncome(models.Model):

    product_type = models.CharField(max_length=50)          # Tipo de Produto
    signer = models.CharField(max_length=100)               # Emissor
    start_date = models.DateField()                         # Data de Entrada
    due_date = models.DateField()                           # Carência
    validity_date = models.DateField()                      # Validade
    tax = models.CharField(max_length=50)                   # Taxa
    available_amount = models.DecimalField()                # Disponível
    guarantee = models.DecimalField()                       # Garantia
    start_amount = models.DecimalField()                    # Valor Aplicado
    position = models.DecimalField()                        # Posição

    def __str__(self):
        return "%s - %s" % (self.product_type, self.signer)


class InvestmentFund(models.Model):
    FUND_TYPE_CHOICES = (
    ('RF', 'Renda Fixa'),
    ('MM', 'Multimercado'),
    ('FI', 'Fundo Imobiliário'),
)

    ativo = models.CharField(max_length=100, unique=True)                   # Ativo
    quota_date = models.DateField()                                         # Data Quota
    quota_value = models.DecimalField()                                     # Valor da Quota
    quote_amount = models.DecimalField()                                    # Quantidade de Quotas
    position = models.DecimalField()                                        # Positção
    net_value = models.DecimalField()                                       # Valor Líquido
    fund_type = models.CharField(max_length=2, choices=FUND_TYPE_CHOICES)   # Tipo de Fundo
    
    def __str__(self):
        return self.ativo

