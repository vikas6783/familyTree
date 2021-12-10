from django.contrib import admin

from .models import Person
from .models import FamilyAddress
from .models import JobLocation
from .models import JobDetail
from .models import CollegeAddress
from .models import EducationDetail

# Register your models here.
admin.site.register(Person)
admin.site.register(FamilyAddress)
admin.site.register(JobLocation)
admin.site.register(JobDetail)
admin.site.register(CollegeAddress)
admin.site.register(EducationDetail)
