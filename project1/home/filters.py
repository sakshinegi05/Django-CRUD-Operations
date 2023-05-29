import django_filters
from .models import Student

class StuCredentials(django_filters.FilterSet):
    class Meta:
        model = Student
        fields='__all__'
    