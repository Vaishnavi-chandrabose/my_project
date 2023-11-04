from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    designation = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'myapp'
