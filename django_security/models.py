from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    role = models.CharField(max_length=30)
    salary = models.FloatField()

    class Meta:
        db_table = 'EMPLOYEE_INFO'

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)