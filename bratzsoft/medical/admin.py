from django.contrib import admin
from .models import Patient, Doctor, Appointment

class PatientAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'phone')
	search_fields = ('first_name', 'last_name', 'phone')

class DoctorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'phone')
	search_fields = ('first_name', 'last_name', 'phone')

class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('date', 'name', 'patient', 'doctor')
	search_fields = ('name', 'patient', 'doctor')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)