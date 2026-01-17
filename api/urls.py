from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter #for viewsets

#urls for viewset
router = DefaultRouter()
router.register('books', views.Books, basename='books') #basename is used only for viewset.ViweSet
router.register('designation',views.DesgnationViewSet)

urlpatterns = [
    path('students/',views.student),
    path('student/<int:pk>/',views.getDetails),
    path('employees/',views.Employees.as_view()),  # .as_view() is required for class-based views
    path('employee/<int:pk>/',views.EmployeeDetail.as_view()),  # .as_view() is required for class-based views
    path('items/',views.Items.as_view()),  # .as_view() is required for class-based views
    path('items/<int:pk>/',views.ItemDetails.as_view()),  # .as_view() is required for class-based views
    path('users/',views.Users.as_view()),  # .as_view() is required for class-based views
    path('users/<int:pk>/',views.UsersDetail.as_view()),  # .as_view() is required for class-based views
    path("", include(router.urls)),
]

