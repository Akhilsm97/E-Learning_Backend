from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(stud_reg)
admin.site.register(Course)
admin.site.register(Course_Topic)
admin.site.register(Login)
admin.site.register(Course_Materials)