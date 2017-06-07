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
    description = models.TextField(max_length=500)
    link = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.link




class Note(BaseModel):
    number = models.CharField(max_length=15)
    version = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    component = models.CharField(max_length=30)
    update_date = models.DateTimeField()
    related_product = models.CharField(max_length=100)
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

class Component(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
