from django.db import models
from bratzsoft.core.models.coremodels import BaseModel
from bratzsoft.core.models.crmmodels import Customer


class LandscapeRole(BaseModel):
    name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

class Product(BaseModel):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return "%s - %s" % (self.name, self.version)



class Host(BaseModel):
    hostname = models.CharField(max_length=100)
    ipv4 = models.GenericIPAddressField()
    customer = models.ForeignKey('core.Customer', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.hostname


class LinkURL(BaseModel):
    description = models.TextField(max_length=500,null=True,blank=True)
    link = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.link

class Component(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500,null=True,blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Note(BaseModel):
    number = models.CharField(max_length=15)
    version = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    update_date = models.DateField()
    related_product = models.ForeignKey('Product', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

    def __str__(self):
        return "%s - %s" % (self.number, self.title)

class System(BaseModel):
    sid = models.CharField(max_length=3)
    instance_number = models.CharField(max_length=2)
    customer = models.ForeignKey('core.Customer', on_delete=models.CASCADE)
    hosts = models.ManyToManyField(Host)
    landscape_role = models.ForeignKey('LandscapeRole', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.sid




class Parameter(BaseModel):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    ref_note = models.ForeignKey('sap.Note',on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

class AbapUser(BaseModel):
    username = models.CharField(max_length=14)
    # To be changed - Password need to be encrypted before save
    password = models.CharField(max_length=10,null=True,blank=True)
    sid = models.ForeignKey('System', on_delete=models.CASCADE)
    client = models.CharField(max_length=3,null=True,blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.username
