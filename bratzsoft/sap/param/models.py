from django.db import models
from bratzsoft.core.models.coremodels import BaseModel


class Parameter(BaseModel):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    ref_note = models.ForeignKey('sap.Note',on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
