from django.urls import path
from . import views
urlpatterns = [
    path('students/',views.student),
    path('student/<int:pk>/',views.getDetails)
]