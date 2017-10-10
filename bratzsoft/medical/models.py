from django.db import models
from bratzsoft.core.models import BaseModel


class Patient(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	birthdate = models.DateField(auto_now_add=True)
	phone = models.CharField(max_length=100)

	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)

class Doctor(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	birthdate = models.DateField(auto_now_add=True)
	phone = models.CharField(max_length=100)

	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)

class Appointment(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	date = models.DateField()
	patient = models.ForeignKey(Patient)
	doctor = models.ForeignKey(Doctor)
	