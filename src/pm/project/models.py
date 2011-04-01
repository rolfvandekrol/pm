from django.db import models

class Employee(models.Model):
  first_name = models.CharField(max_length=255)
  
  last_name = models.CharField(max_length=255)
  
  username = models.CharField(max_length=255)
  
  password = models.CharField(max_length=128)

class WorkingHours(models.Model):
  employee = models.ForeignKey(Employee)
  
  from_date = models.DateField()
  to_date = models.DateField(blank = True)
  
  sunday = models.IntegerField(default = 0)
  monday = models.IntegerField(default = 8)
  tuesday = models.IntegerField(default = 8)
  wednesday = models.IntegerField(default = 8)
  thursday = models.IntegerField(default = 8)
  friday = models.IntegerField(default = 8)
  saterday = models.IntegerField(default = 0)
