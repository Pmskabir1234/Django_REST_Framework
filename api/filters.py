import django_filters
from blog.models import Blog
from employees.models import User


class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='blog_title',lookup_expr='iexact')
    # use of iexact in lookup_expr handles the case insenivity
    id = django_filters.RangeFilter(field_name='id')

    class Meta:
        model = Blog
        fields = ['id','title']


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='user_name', lookup_expr='icontains', label='Username')
    email = django_filters.CharFilter(field_name ='user_email', lookup_expr='icontains', label='User Email')
    # use of icontains helps searching on the basis of substring presence

    #now we'll see how to use strings(user_id) as filter
    uid_min = django_filters.CharFilter(method='myfilter', label = 'From User ID')
    uid_max = django_filters.CharFilter(method='myfilter', label = 'To User ID')


    class Meta:
        model = User
        fields = ['name','email','uid_min','uid_max']

    def myfilter(self,queryset,name,value):
        if name == 'uid_min':
            return queryset.filter(user_id__gte=value)
        elif name == 'uid_max':
            return queryset.filter(user_id__lte=value)
        return queryset
    