from django.db import models
from django.conf import settings
from .coremodels import BaseModel

class Customer(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    account = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    #user =

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
