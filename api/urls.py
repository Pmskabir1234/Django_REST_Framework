from django.urls import path
from . import views
urlpatterns = [
    path('students/',views.student),
    path('student/<int:pk>/',views.getDetails),
    path('employees/',views.Employees.as_view()),  # .as_view() is required for class-based views
]