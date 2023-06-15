from django.contrib import admin
from .models import Employees,Department,Role

# Register your models here.
admin.site.register(Employees)
admin.site.register(Role)
admin.site.register(Department)