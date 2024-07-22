from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from members.models import *

# Register your models here.



admin.site.register(CustomUser)
admin.site.register(Role)
admin.site.register(WorkStatus)
admin.site.register(Work)

