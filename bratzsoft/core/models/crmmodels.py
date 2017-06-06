from django.db import models
from .coremodels import BaseModel

class Customer(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    #user =

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
