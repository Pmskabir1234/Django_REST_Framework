from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=6)
    emp_name = models.CharField(max_length=25)
    emp_designation = models.CharField(max_length=30)

    def __str__(self):
        return self.emp_name
    
class Item(models.Model):
    item_id = models.CharField(max_length=5)
    item_name = models.CharField(max_length=50)
    item_price = models.FloatField(max_length=7)

    def __str__(self):
        return self.item_name
