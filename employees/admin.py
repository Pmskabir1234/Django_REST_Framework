from django.contrib import admin
from .models import Employee
from .models import Item,User, Book

# Register your models here.
admin.site.register(Employee)
admin.site.register(Item)
admin.site.register(User)
admin.site.register(Book)
