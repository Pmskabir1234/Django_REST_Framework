import django_filters
from blog.models import Blog

class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='blog_title',lookup_expr='iexact')
    # use of iexact in lookup_expr handles the case insenivity

    class Meta:
        model = Blog
        fields = ['title']