from django.contrib import admin

# Register your models here.
#from .models import Choice, Question
from .models import Student


admin.site.register(Student)
#admin.site.register(Question)
#admin.site.register(Choice)