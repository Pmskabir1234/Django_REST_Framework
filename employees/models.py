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

class User(models.Model):
    user_id = models.CharField(max_length=5)
    user_name = models.CharField(max_length=40)
    user_email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user_name
    
class Book(models.Model):
    book_name = models.CharField(max_length=50)
    book_price = models.FloatField(max_length=5)

    def __str__(self):
        return self.book_name

class Designation(models.Model):
    position = models.CharField(max_length=30)
    salary = models.IntegerField(max_length=6)

    def __str__(self):
        return self.position