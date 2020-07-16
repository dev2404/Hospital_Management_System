from django.contrib import admin
from myapp.models import Appointment, Appointment1, Doctor, Patient
# Register your models here.

admin.site.register(Appointment)
admin.site.register(Appointment1)
admin.site.register(Doctor)
admin.site.register(Patient)


