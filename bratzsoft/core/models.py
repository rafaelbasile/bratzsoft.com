from django.db import models
from django.utils.six import with_metaclass
import datetime


class BaseModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        super().save(*args, **kwargs)
