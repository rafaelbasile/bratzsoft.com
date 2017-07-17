"""Investments Model."""


from django.db import models


"""
Stock Model.
"""


class Stock(models.Model):
    name = models.CharField(max_length=150)
    symbol = models.CharField(max_length=9)
    sector = models.CharField(max_length=100)
    subSector = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    market_segment = models.CharField(max_length=100)
    listing_segment = models.CharField(max_length=100)
    site = models.UrlField()
    head_quarter = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    majority = models.CharField(max_length=100)


"""
Stock Model.
"""


class StockQuote(models.Model):
    stock = models.ForeignField(Stock)
    date = models.DateField()
    value = models.FloatField()
