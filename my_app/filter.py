import django_filters
from .models import Customer
from django_filters import CharFilter
class CustomerFilter(django_filters.FilterSet):
    customername = CharFilter(field_name = "customername",lookuo_expr = 'icontains' )
    class Meta:
        model = Customer
        fields = ['customerid']