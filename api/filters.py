import django_filters
from blog.models import Blog
from employees.models import User


class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='blog_title',lookup_expr='iexact')
    # use of iexact in lookup_expr handles the case insenivity

    class Meta:
        model = Blog
        fields = ['title']


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='user_name', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name ='user_email', lookup_expr='icontains')
    # use of icontains helps searching on the basis of substring presence

    class Meta:
        model = User
        fields = ['name','email']
    