from django.db import models
from .coremodels import BaseModel
from .crmmodels import Customer

class Host(BaseModel):
    hostname = models.CharField(max_length=100)
    ipv4 = models.GenericIPAddressField()
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE,)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.hostname


class LinkURL(BaseModel):
    description = models.TextField(max_length=500)
    link = models.URLField()

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
    category = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)



class System(BaseModel):
    sid = models.CharField(max_length=3)
    instance_number = models.CharField(max_length=2)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    hosts = models.ManyToManyField(Host)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.sid
