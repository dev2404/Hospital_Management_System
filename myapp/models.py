from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length =122) 
    email = models.CharField(max_length =122)
    phone = models.CharField(max_length =12)
    address = models.CharField(max_length =122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.email

class Doctor(models.Model):
    name = models.CharField(max_length =122) 
    email = models.CharField(max_length =122)
    phone = models.CharField(max_length =12)
    address = models.CharField(max_length =122)
    special = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length =122) 
    gender = models.CharField(max_length =12)
    phone = models.CharField(max_length =12)
    address = models.CharField(max_length =122)

    def __str__(self):
        return self.name        

class Appointment1(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE) 
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)        
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.doctor.name + "--" + self.patient.name 

 
    
           